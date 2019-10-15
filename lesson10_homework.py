class Gadget:  # brand, model, year

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def gadget_info(self):
        return f"{self.brand}, {self.model}, {self.year}" # brand, model, year


class Phone(Gadget):    # applications -> list, contacts -> list,
                        # settings -> + (inherit gadget)

    def __init__(self, brand, model, year, applications, contacts, settings):
        super().__init__(brand, model, year)
        self.applications = applications
        self.contacts = contacts
        self.settings = settings

    def add_app(self, app):
        if app not in self.applications:
            self.applications.append(app)
        else:
            print('Application already exists')

    def del_app(self, app):
        if app in self.applications:
            self.applications.remove(app)
            print('Application removed')

    def add_contact(self, contact):
        if contact not in self.contacts:
            self.contacts.append(contact)
        else:
            print('Contact already exists')

    def del_contact(self, contact):
        self.contacts.remove(contact)
        print('Contact removed')

    def edit_settings(self, **settings):
        self.settings.update(settings)


class Computer(Gadget):  # OS, applications, trash

    def __init__(self, brand, model, year, os, applications):
        super().__init__(brand, model, year)
        self.os = os
        self.applications = applications
        self.trash = []

    def add_app(self, app):
        if app not in self.applications:
            self.applications.append(app)
        else:
            print('Application already exists')

    def del_app(self, app):
        self.applications.remove(app)
        print(f"Application {app} was sent to trash")
        self.trash.append(app)

    def explore_trash(self):
        return ', '.join(self.trash)

    def remove_trash(self):
        self.trash.clear()


class TV(Gadget):  # channels, settings

    def __init__(self, brand, model, year, channels, settings):
        super().__init__(brand, model, year)
        self.channels = channels
        self.settings = settings

    def add_chanel(self, channel):
        for chan in channel:
            if chan not in self.channels:
                self.channels.append(chan)
        else:
            print('Channel exists')

    def del_chanel(self, channel):
        self.channels.remove(channel)

    def edit_settings(self, **settings):
        self.settings.update(settings)


p1 = Phone('iPhone', '11 pro', 2019, ['Telegram'], ['John'], {'Theme': 'Dark'})

print(p1.settings)
p1.edit_settings(**{'Mode': 'Silent'})
print(p1.settings)

c1 = Computer('Macbook', 'Pro', 2017, 'Mojave', ['Pycharm', 'Evernote'])

c1.add_app('Telegram')
print(c1.applications)

c1.del_app('Telegram')

print(c1.applications)

print(c1.explore_trash())

c1.remove_trash()

print(c1.explore_trash())

t1 = TV('LG', 'Flat', 2019, ['MTV', 'CBS'], {'Volume': 'Loud'})

t1.add_chanel(['1+1', 'CBS', 'Fox News'])
print(t1.channels)

t1.del_chanel('1+1')
print(t1.channels)

t1.edit_settings(**{'Volume': 'Loud', 'Brightness': 'Low'})
print(t1.settings)