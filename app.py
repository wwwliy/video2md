"""Video2MD application entry point."""

from core.application import Application


def main() -> None:
    """Run the Video2MD command-line application."""
    Application().run()


if __name__ == "__main__":
    main()
