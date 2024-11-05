interface IOperation<T>
{
    void Handle(T data);
}

class Pipeline<T> : IOperation<T>
{
    private readonly List<IOperation<T>> operations = new List<IOperation<T>>();

    public void Add(IOperation<T> operation) => operations.Add(operation);

    public void Handle(T data)
    {
        foreach (var operation in operations)
        {
            operation.Handle(data);
        }
    }
}

class Operation<T> : IOperation<T>
{
    private readonly Action<T> action;

    public Operation(Action<T> action)
    {
        this.action = action;
    }

    public void Handle(T data) => action(data);
}

class ReverseOperation : IOperation<string>
{
    public void Handle(string data)
    {
        var charArray = data.ToCharArray();
        Array.Reverse(charArray);
        Console.WriteLine(new string(charArray));
    }
}

var pipeline = new Pipeline<string>();

pipeline.Add(new Operation<string>(data =>
    Console.WriteLine($"The string {data} contains {data.Length} characters.")
));

pipeline.Add(new ReverseOperation());

pipeline.Handle("Hello, World!");