class widget:
    """ Models a manufactured item. """
    serial_number_source = 0  # class varialbe

    def __init__(self) -> None:
        """make a widget with a unique serial number. """
        self.serial_number = widget.serial_number_source
        widget.serial_number_source += 1

    def get_serial_number(self):
        """ returns the widget's serial number. """
        return self.serial_number


if __name__ == "__main__":
    widget_list = []
    for iterator in range(10):
        widget_list.append(widget())

    for widget in widget_list:
        print(widget.get_serial_number(), end=" ")
        print(widget.serial_number_source, end=" ")

    print()
