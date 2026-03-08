from flask import Blueprint, render_template, request

portagiro_bp = Blueprint("portagiro", __name__)

@portagiro_bp.route("/portagiro")
def portagiro():
    return("i painho cheiroso e legal ksks")