"""Flask blueprint for race endpoints."""
import logging
from flask import Blueprint, jsonify

from ..models.race import Race

logger = logging.getLogger(__name__)

races_bp = Blueprint(name="races", import_name=__name__)


@races_bp.route("/", methods=["GET"])
def list_races():
    """Return a list of all available races.

    Returns:
        JSON list of all races with their stat bonuses.
    """
    races = Race.query.all()
    logger.info("Retrieved %d races.", len(races))
    return jsonify([r.to_dict() for r in races])


@races_bp.route("/<int:race_id>", methods=["GET"])
def get_race(race_id: int):
    """Return a single race by ID.

    Args:
        race_id: The ID of the race to retrieve.

    Returns:
        JSON of the race, or 404 if not found.
    """
    race = Race.query.get(race_id)
    if race is None:
        return jsonify({"error": f"Race ID {race_id} not found."}), 404
    return jsonify(race.to_dict()), 200
