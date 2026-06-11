"""Flask blueprint for character class endpoints."""
import logging
from flask import Blueprint, jsonify

from ..models.character_class import CharacterClass

logger = logging.getLogger(__name__)

classes_bp = Blueprint(name="classes", import_name=__name__)


@classes_bp.route("/", methods=["GET"])
def list_classes():
    """Return a list of all available character classes.

    Returns:
        JSON list of all character classes with their stats.
    """
    classes = CharacterClass.query.all()
    logger.info("Retrieved %d classes.", len(classes))
    return jsonify([c.to_dict() for c in classes])


@classes_bp.route("/<int:class_id>", methods=["GET"])
def get_class(class_id: int):
    """Return a single character class by ID.

    Args:
        class_id: The ID of the character class to retrieve.

    Returns:
        JSON of the character class, or 404 if not found.
    """
    character_class = CharacterClass.query.get(class_id)
    if character_class is None:
        return jsonify({"error": f"Class ID {class_id} not found."}), 404
    return jsonify(character_class.to_dict()), 200