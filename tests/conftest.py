import pytest
from app import create_app
from app.models.database import db as _db
from app.models.character import Character
from app.models.character_class import CharacterClass
from app.models.race import Race


@pytest.fixture(scope="session")
def app():
    flask_app = create_app(testing=True)
    with flask_app.app_context():
        _db.create_all()
        _seed_data()
        yield flask_app
        _db.drop_all()


def _seed_data():
    if CharacterClass.query.count() == 0:
        classes = [
            CharacterClass(
                name="Swordsman",
                hit_die=10,
                primary_stat="strength",
                description="A master of blade combat who fights with power and precision, like the Pirate Hunter Zoro.",
            ),
            CharacterClass(
                name="Navigator",
                hit_die=6,
                primary_stat="intelligence",
                description="A tactical genius who uses knowledge and weather to outsmart any enemy, like the Cat Burglar Nami.",
            ),
            CharacterClass(
                name="Sniper",
                hit_die=8,
                primary_stat="dexterity",
                description="A long-range specialist with incredible aim and resourcefulness, like the King of Snipers Usopp.",
            ),
            CharacterClass(
                name="Cook",
                hit_die=8,
                primary_stat="dexterity",
                description="A powerful fighter who uses only their legs in combat and never wastes their hands, like the Black Leg Sanji.",
            ),
            CharacterClass(
                name="Doctor",
                hit_die=8,
                primary_stat="wisdom",
                description="A brilliant medic who can heal any wound and fight with surprising strength, like the Cotton Candy Lover Chopper.",
            ),
            CharacterClass(
                name="Devil Fruit User",
                hit_die=6,
                primary_stat="charisma",
                description="A fighter with an unpredictable and powerful Devil Fruit ability, like the Straw Hat Luffy.",
            ),
            CharacterClass(
                name="Shipwright",
                hit_die=10,
                primary_stat="constitution",
                description="A powerhouse builder and fighter with a cyborg body, like the Cyborg Franky.",
            ),
            CharacterClass(
                name="Musician",
                hit_die=6,
                primary_stat="charisma",
                description="A soulful fighter who returns from death itself to keep the crews spirits high, like Soul King Brook.",
            ),
            CharacterClass(
                name="Archaeologist",
                hit_die=6,
                primary_stat="intelligence",
                description="A genius scholar who can sprout arms from any surface to overwhelm enemies, like the Demon Child Robin.",
            ),
            CharacterClass(
                name="Pirate Captain",
                hit_die=8,
                primary_stat="charisma",
                description="A bold and inspiring leader who rallies their crew through impossible odds.",
            ),
            CharacterClass(
                name="Marine",
                hit_die=10,
                primary_stat="strength",
                description="A disciplined enforcer of justice who fights for the World Government.",
            ),
            CharacterClass(
                name="Bounty Hunter",
                hit_die=10,
                primary_stat="dexterity",
                description="A ruthless tracker who hunts pirates for fame and fortune across the seas.",
            ),
        ]
        _db.session.add_all(classes)

    if Race.query.count() == 0:
        races = [
            Race(
                name="Human",
                description="The most common race in the One Piece world. Versatile and found on every sea.",
                strength_bonus=1,
                dexterity_bonus=1,
                constitution_bonus=1,
                intelligence_bonus=1,
                wisdom_bonus=1,
                charisma_bonus=1,
            ),
            Race(
                name="Fishman",
                description="Powerful aquatic warriors with incredible physical strength. Ten times stronger than humans.",
                strength_bonus=2,
                constitution_bonus=2,
            ),
            Race(
                name="Giant",
                description="Massive warriors from Elbaf with overwhelming strength and endurance.",
                strength_bonus=3,
                constitution_bonus=2,
                charisma_bonus=-1,
            ),
            Race(
                name="Mink",
                description="Animal-human hybrids from Zou who can use Electro and are strongest at night.",
                dexterity_bonus=2,
                wisdom_bonus=1,
            ),
            Race(
                name="Cyborg",
                description="Humans enhanced with scientific modifications for incredible durability, like Franky.",
                constitution_bonus=3,
                intelligence_bonus=1,
                charisma_bonus=-2,
            ),
            Race(
                name="Lunarian",
                description="A nearly extinct race from the Red Line with incredible resilience and fire abilities.",
                strength_bonus=1,
                dexterity_bonus=1,
                constitution_bonus=3,
            ),
            Race(
                name="Longarm Tribe",
                description="A tribe with double-jointed arms giving them extraordinary reach and dexterity.",
                dexterity_bonus=3,
                intelligence_bonus=1,
            ),
            Race(
                name="Longleg Tribe",
                description="A tribe with incredibly long legs giving them powerful kicks and swift movement.",
                dexterity_bonus=2,
                strength_bonus=1,
            ),
            Race(
                name="Tontatta",
                description="Tiny but fierce dwarves from Green Bit with superhuman speed and a strong sense of justice.",
                dexterity_bonus=3,
                wisdom_bonus=1,
                strength_bonus=-1,
            ),
            Race(
                name="Skypiean",
                description="Winged inhabitants of Skypiea with deep wisdom and knowledge of the ancient world.",
                wisdom_bonus=2,
                dexterity_bonus=1,
            ),
        ]
        _db.session.add_all(races)

    _db.session.commit()


@pytest.fixture(scope="session")
def warrior_class(app):
    return CharacterClass.query.filter_by(name="Swordsman").first()


@pytest.fixture(scope="session")
def human_race(app):
    return Race.query.filter_by(name="Human").first()


@pytest.fixture
def sample_character(app, warrior_class, human_race):
    character = Character(
        name="Test Swordsman",
        level=1,
        class_id=warrior_class.id,
        race_id=human_race.id,
        strength=16,
        dexterity=14,
        constitution=12,
        intelligence=10,
        wisdom=8,
        charisma=10,
    )
    _db.session.add(character)
    _db.session.commit()
    yield character
    _db.session.delete(character)
    _db.session.commit()


@pytest.fixture
def db(app):
    return _db


@pytest.fixture
def client(app):
    return app.test_client()