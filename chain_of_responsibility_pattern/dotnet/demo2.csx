interface IOperation<T>
{
    bool Invoke(T data);
}

class Pipeline<T> : IOperation<T>
{
    private readonly List<IOperation<T>> operations = new List<IOperation<T>>();

    public void Add(IOperation<T> operation) => operations.Add(operation);

    public bool Invoke(T data)
    {
        foreach (var operation in operations)
        {
            if (!operation.Invoke(data))
            {
                Console.WriteLine("The operation failed.");
                return false;
            }
        }

        return true;
    }
}

class Operation<T> : IOperation<T>
{
    private readonly Func<T, bool> action;

    public Operation(Func<T, bool> action)
    {
        this.action = action;
    }

    public bool Invoke(T data) => action(data);
}

class CheckNotNullOperation : IOperation<string>
{
    public bool Invoke(string data)
    {
        if (data == null)
        {
            Console.WriteLine("The string is null.");
            return false;
        }

        return true;
    }
}

class CheckStringLengthOperation : IOperation<string>
{
    private readonly int maxLength;

    public CheckStringLengthOperation(int maxLength)
    {
        this.maxLength = maxLength;
    }

    public bool Invoke(string data)
    {
        if (data.Length > maxLength)
        {
            Console.WriteLine($"The string exceeds the maximum length of {maxLength}.");
            return false;
        }

        return true;
    }
}

var pipeline = new Pipeline<string>();

pipeline.Add(new CheckNotNullOperation());

pipeline.Add(new CheckStringLengthOperation(10));

pipeline.Invoke("Hello, World!");