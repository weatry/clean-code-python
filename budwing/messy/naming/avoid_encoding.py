"""
There are some naming encoding conventions due to historical reasons or language limitations.
For example, Hungarian Notation prefixes variable names with type information (e.g., "strName" for a string).
This practice can lead to confusion and reduced code readability, especially in modern programming languages.
Because of advancements in IDEs and type inference, such encoding is often unnecessary and can clutter code.
Instead, it's generally better to use clear and descriptive names that convey the purpose of the variable.

Another example is using prefixes like "m_" for member variables or "s_" for static variables.
While these conventions can help distinguish variable scopes, they can also make code harder to read and maintain.
Modern programming practices favor using language features (like "this" keyword) and proper naming conventions.

Some developers may use encoding to indicate variable roles, such as "is" for booleans (e.g., "isActive").
While this can enhance clarity, overuse of such prefixes can lead to verbose and less readable code.
"""

class AvoidEncoding:
    """Messy example that demonstrates encoding-style names.

    Attributes:
        str_name: string-like name using Hungarian prefix.
        m_age: member-encoded age.
        is_active: boolean encoded with 'is' prefix.
    """

    SLOGAN: str = "AVOID ENCODING"

    str_name: str
    m_age: int
    is_active: bool

    def __init__(self) -> None:
        # Example of Hungarian Notation encoding.
        # The prefix "str" indicates that the variable is a string.
        self.str_name: str = "John Doe"

        # Example of member variable encoding.
        self.m_age: int = 30

        # Example of boolean variable encoding.
        self.is_active: bool = True


class IRunnable:
    """Messy-style interface placeholder (kept for example).

    Implementers should provide a run() method.
    """

    def run(self) -> None:  # pragma: no cover - example only
        raise NotImplementedError


class RunnableImpl(IRunnable):
    """Simple runnable implementation used in the messy example."""

    def run(self) -> None:  # pragma: no cover - prints for demo
        print("Running...")
