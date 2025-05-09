"""
This module contains signal handlers for the `Correction` model.
"""
import shutil
import os
import logging
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from iagscore import settings
from .models import Correction

logger = logging.getLogger("corrections.signals")
logger.setLevel(logging.CRITICAL)
logger.propagate = False


@receiver(pre_delete, sender=Correction)
def delete_correction_folder(sender, instance, **kwargs):
    """
    Delete the files in the folder of the correction folder when the
    corrections is deleted

    Parameters:
        sender: The model class that sent the signal (`Correction`).
        instance: The instance of the `Correction` model being deleted.
        **kwargs: Additional keyword arguments passed by the signal.

    """

    base_path = settings.MEDIA_ROOT
    folder_path = os.path.join(base_path, instance.folder_path)

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        try:
            shutil.rmtree(folder_path)
            logger.info("Carpeta eliminada: %s", folder_path)
        except OSError as e:
            logger.error("Error al eliminar la carpeta %s: %s", folder_path, e)

    else:
        logger.warning("La carpeta no existe o no es un directorio.")
