from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import subprocess
import json
import os

@csrf_exempt
def index(request):
    publicaciones = None
    total_reacciones = 0
    total_comentarios = 0

    if request.method == 'POST':
        face_name = request.POST.get('faceName')
        if face_name:
            script_path = os.path.join(settings.BASE_DIR, 'core', 'scrapper-face.py')
            
            try:
                result = subprocess.run(['python', script_path, face_name], check=True, capture_output=True, text=True)
                print("Scrapper Output:", result.stdout)
            except subprocess.CalledProcessError as e:
                print("❌ Error ejecutando el scrapper:", e)
                print("STDERR:", e.stderr)
                return render(request, 'core/index.html', {
                    'error': 'Error ejecutando el scrapper. Ver consola para más detalles.'
                })

            json_path = os.path.join(settings.BASE_DIR, 'core', 'static', 'core', 'publicaciones.json')
            if os.path.exists(json_path):
                try:
                    with open(json_path, 'r', encoding='utf-8') as f:
                        publicaciones = json.load(f)

                        # Calcular totales
                        for pub in publicaciones:
                            total_reacciones += pub.get("reacciones") or 0
                            total_comentarios += pub.get("comentarios") or 0

                except json.JSONDecodeError:
                    print("⚠️ Error al leer el JSON generado por el scrapper.")
                    publicaciones = None

    return render(request, 'core/index.html', {
        'publicaciones': publicaciones,
        'total_reacciones': total_reacciones,
        'total_comentarios': total_comentarios,
    })
