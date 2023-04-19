class subject:
    def __init__(self) -> None:
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()


class concreteSubject(subject):
    def __init__(self) -> None:
        super().__init__()
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify()


class observer:
    def update(self):
        pass

class concreteObserver(observer):
    def __init__(self, subject) -> None:
        self._subject = subject
        self._subject.attach(self)


    def update(self):
        print("Observer's state has been updated to : {}".format(self._subject.state))
    
if __name__ == "__main__":
    subject = concreteSubject()
    observer1 = concreteObserver(subject)
    observer2 = concreteObserver(subject)

    subject.state = 123
    subject.detach(observer1)

    subject.state = 456
