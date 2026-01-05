def dossier_serializer(obj):
    return {
        "id": obj.id,
        "nom": obj.nom,
        "description": obj.description,
        "date_creation": obj.date_creation.isoformat(),
    }