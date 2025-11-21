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
    """Clean example recommending clearer names instead of encoded prefixes.

    Attributes:
        name: the person's name.
        age: the person's age.
        active: whether the person is active.
    """

    SLOGAN: str = "AVOID ENCODING"

    name: str
    age: int
    active: bool

    def __init__(self) -> None:
        """
        Compared to strName, name is a more descriptive and clearer variable name.
        Compared to m_age, age is a more descriptive and clearer variable name.
        Compared to isActive, active is a more concise variable name while still conveying the boolean nature.
        """
        self.name: str = "John Doe"
        self.age: int = 30
        self.active: bool = True


class Runnable:
    """Clean interface-like base with run() method."""

    def run(self) -> None:  # pragma: no cover - example only
        raise NotImplementedError


class PrintRunnable(Runnable):
    """Descriptive implementation name for a runnable that prints."""

    def run(self) -> None:  # pragma: no cover - prints for demo
        print("Running...")
