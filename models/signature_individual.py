# model used for signature_individual table
from .db import db
from utils.serializer import Serializer

class Individual(db.Model, Serializer):
    __tablename__ = 'signature_individual'
    
    signature = db.Column(db.String, primary_key=True)
    outcome = db.Column(db.String, primary_key=True)
    model = db.Column(db.String, primary_key=True)
    study = db.Column(db.String, primary_key=True)
    primary_tissue = db.Column(db.String, primary_key=True)
    sequencing = db.Column(db.String)
    n = db.Column(db.Integer)
    effect_size = db.Column(db.Float)
    se = db.Column(db.Float)
    _95ci_low = db.Column(db.Float)
    _95ci_high = db.Column(db.Float)
    pval = db.Column(db.Float)

    def serialize(self):
        serialized = Serializer.serialize(self)
        return serialized

