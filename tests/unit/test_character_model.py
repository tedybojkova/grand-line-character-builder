import pytest


class TestStatModifiers:

    def test_strength_modifier(self, sample_character):
        assert sample_character.strength_modifier == 3

    def test_dexterity_modifier(self, sample_character):
        assert sample_character.dexterity_modifier == 2

    def test_wisdom_modifier_negative(self, sample_character):
        assert sample_character.wisdom_modifier == -1

    def test_intelligence_modifier_zero(self, sample_character):
        assert sample_character.intelligence_modifier == 0


class TestMaxHitPoints:

    def test_level1_hp(self, sample_character):
        assert sample_character.max_hit_points == 11

    def test_higher_level_increases_hp(self, sample_character):
        sample_character.level = 5
        assert sample_character.max_hit_points == 55


class TestArmourClass:

    def test_ac_equals_ten_plus_dex_mod(self, sample_character):
        expected = 10 + sample_character.dexterity_modifier
        assert sample_character.armour_class == expected


class TestProficiencyBonus:

    @pytest.mark.parametrize("level,expected", [
        (1, 2), (4, 2),
        (5, 3), (8, 3),
        (9, 4), (12, 4),
        (17, 6), (20, 6),
    ])
    def test_proficiency_bonus(self, sample_character, level, expected):
        sample_character.level = level
        assert sample_character.proficiency_bonus == expected


class TestBounty:

    def test_default_bounty_is_zero(self, sample_character):
        assert sample_character.bounty == 0

    def test_bounty_can_be_set(self, sample_character):
        sample_character.bounty = 120_000_000
        assert sample_character.bounty == 120_000_000

    def test_bounty_cannot_be_negative(self, sample_character):
        from app.services.character_service import CharacterService
        service = CharacterService()
        with pytest.raises(ValueError):
            service._validate_bounty(-1)

    def test_bounty_cannot_exceed_max(self, sample_character):
        from app.services.character_service import CharacterService
        service = CharacterService()
        with pytest.raises(ValueError):
            service._validate_bounty(9_999_999_999)