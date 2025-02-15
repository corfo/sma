###

# python manage.py load_comunas app_ppda/data/comunas.csv

###
import csv
from django.core.management.base import BaseCommand
from app_ppda.models import Comuna
from os import getcwd
class Command(BaseCommand):
    help = "Carga comunas desde un archivo CSV"
    cwd = getcwd()
    print(f"📂 Directorio actual: {cwd}")

    def add_arguments(self, parser):
        parser.add_argument("archivo", type=str, help="Ruta del archivo CSV")

    def handle(self, *args, **kwargs):
        archivo_csv = kwargs["archivo"]

        try:
            with open(archivo_csv, newline="", encoding="utf-8") as archivo:
                reader = csv.reader(archivo)
                next(reader)  # Saltar encabezados
                comunas = [Comuna(nombre=row[0], codigo=row[1]) for row in reader]

            Comuna.objects.bulk_create(comunas)
            self.stdout.write(self.style.SUCCESS(f"Se cargaron {len(comunas)} comunas correctamente."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error al cargar comunas: {e}"))
