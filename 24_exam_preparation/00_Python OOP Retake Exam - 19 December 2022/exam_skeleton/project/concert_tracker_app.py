from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    valid_musician_type = ["Guitarist", "Drummer", "Singer"]

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.valid_musician_type:
            raise ValueError("Invalid musician type!")

        if any(m.name == name for m in self.musicians):
            raise Exception(f"{name} is already a musician!")

        if musician_type == "Guitarist":
            musician = Guitarist(name, age)
        elif musician_type == "Drummer":
            musician = Drummer(name, age)
        else:
            musician = Singer(name, age)

        self.musicians.append(musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if any(b.name == name for b in self.bands):
            raise Exception(f"{name} band is already created!")
        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        if any(c.place == place for c in self.concerts):
            concert = [c for c in self.concerts if c.place == place][0]
            raise Exception(f"{place} is already registered for {concert.genre} concert!")
        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{concert.genre} concert in {concert.place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        if not any(m.name == musician_name for m in self.musicians):
            raise Exception(f"{musician_name} isn't a musician!")
        if not any(b.name == band_name for b in self.bands):
            raise Exception(f"{band_name} isn't a band!")
        musician = [m for m in self.musicians if m.name == musician_name][0]
        band = [b for b in self.bands if b.name == band_name][0]
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        if not any(b.name == band_name for b in self.bands):
            raise Exception(f"{band_name} isn't a band!")
        band = [b for b in self.bands if b.name == band_name][0]
        if not any(m.name == musician_name for m in band.members):
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        musician = [m for m in band.members if m.name == musician_name][0]
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        member_of_singer = False
        member_of_drummer = False
        member_of_guitarist = False
        for member in band.members:
            if member.__class__.__name__ == 'Singer':
                member_of_singer = True
            elif member.__class__.__name__ == "Drummer":
                member_of_drummer = True
            elif member.__class__.__name__ == "Guitarist":
                member_of_guitarist = True

        if member_of_singer is False or member_of_drummer is False or member_of_guitarist is False:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = [c for c in self.concerts if c.place == concert_place][0]

        drummer_skills = False
        singer_skills = False
        singer_skills_two = False
        guitarist_skills = False

        if concert.genre == "Rock":
            for member in band.members:
                if 'play the drums with drumsticks' in member.skills:
                    drummer_skills = True
                elif 'sing high pitch notes' in member.skills:
                    singer_skills = True
                elif 'play rock' in member.skills:
                    guitarist_skills = True
            if drummer_skills is False or singer_skills is False or guitarist_skills is False:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Metal':
            for member in band.members:
                if 'play the drums with drumsticks' in member.skills:
                    drummer_skills = True
                elif 'sing low pitch notes' in member.skills:
                    singer_skills = True
                elif 'play metal' in member.skills:
                    guitarist_skills = True
            if drummer_skills is False or singer_skills is False or guitarist_skills is False:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Jazz':
            for member in band.members:
                if 'play the drums with drum brushes' in member.skills:
                    drummer_skills = True
                if 'sing high pitch notes' in member.skills:
                    singer_skills = True
                if 'sing low pitch notes' in member.skills:
                    singer_skills_two = True
                if 'play jazz' in member.skills:
                    guitarist_skills = True
            if drummer_skills is False or singer_skills is False or singer_skills_two is False or guitarist_skills is False:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."