from typing import Callable, Any

# Define the type for middleware functions
Middleware = Callable[[dict[str, Any], Callable[[], Any]], Any]


# Build a middleware pipeline
def build_pipeline(middlewares: list[Middleware]) -> Callable[[dict[str, Any]], Any]:
    def wrap(data: dict[str, Any]) -> Any:
        def create_next(mw_index: int) -> Callable[[], Any]:
            if mw_index < len(middlewares) - 1:
                return lambda: middlewares[mw_index](data, create_next(mw_index + 1))
            else:
                return lambda: middlewares[mw_index](data)

        return create_next(0)()

    return wrap
