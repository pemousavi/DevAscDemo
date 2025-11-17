from typing import Callable, Iterable, List, Any

"""
Simple feature module.

Place this file at: /Users/pejman/code/DevAscDemo/Features/myfeatures.py
"""



class SimpleFeature:
    """
    A small feature object that can be enabled/disabled and applies a transformation
    to input data when active.
    """

    def __init__(self, name: str, transform: Callable[[Any], Any] = lambda x: x):
        self.name = name
        self._enabled = True
        self.transform = transform

    def enable(self) -> None:
        """Enable the feature."""
        self._enabled = True

    def disable(self) -> None:
        """Disable the feature."""
        self._enabled = False

    def toggle(self) -> None:
        """Toggle enabled state."""
        self._enabled = not self._enabled

    def enabled(self) -> bool:
        """Return whether the feature is enabled."""
        return self._enabled

    def process(self, items: Iterable[Any]) -> List[Any]:
        """
        Process an iterable of items with the feature's transform if enabled.
        If disabled, returns the items unchanged as a list.
        """
        result = [self.transform(i) for i in items] if self._enabled else list(items)
        return result


# Example usage when run as a script
if __name__ == "__main__":
    f = SimpleFeature("uppercase", transform=lambda s: str(s).upper())
    samples = ["hello", "world", "feature"]

    print("Enabled:", f.enabled())
    print("Processed:", f.process(samples))

    f.disable()
    print("Enabled after disable:", f.enabled())
    print("Processed when disabled:", f.process(samples))