"""TURLink Radio Management & Link Monitor entry point."""

from __future__ import annotations

import sys


def main() -> int:
    try:
        from PySide6.QtWidgets import QApplication
    except ImportError:
        print("PySide6 bulunamadı. Önce: python -m pip install -r requirements.txt")
        return 1

    from ui.main_window import MainWindow
    from ui.theme import application_stylesheet

    app = QApplication(sys.argv)
    app.setApplicationName("TURLink Radio Management & Link Monitor")
    app.setOrganizationName("TURLink")
    app.setStyleSheet(application_stylesheet())
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
