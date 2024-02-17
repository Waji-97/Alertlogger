from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Alert
import json
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def alert_receiver(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            # Extract alert details from the JSON payload
            alerts = data.get('alerts', [])
            for alert in alerts:
                status = alert.get('status')
                labels = alert.get('labels', {})
                annotations = alert.get('annotations', {})
                starts_at = alert.get('startsAt')
                ends_at = alert.get('endsAt')

                # Process and save the alert data
                alert_instance = Alert.objects.create(
                    name=labels.get('alertname'),
                    severity=labels.get('severity'),
                    summary=annotations.get('summary'),
                    description=annotations.get('description'),
                    created_at=starts_at
                )
                alert_instance.save()

            logger.info("Received and processed alerts: %s", alerts)
            return JsonResponse({'status': 'received'})
        except json.JSONDecodeError as e:
            logger.error("Error decoding JSON data: %s", e)
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except Exception as e:
            logger.error("Error processing alerts: %s", e)
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

def get_alerts(request):
    alerts = Alert.objects.all().order_by('-created_at').values('name', 'severity', 'summary', 'description', 'created_at')
    return JsonResponse(list(alerts), safe=False)


def index(request):
    alerts = Alert.objects.all()
    return render(request, 'index.html', {'alerts': alerts})

@csrf_exempt
def delete_entries(request):
    if request.method == 'POST':
        # Delete all entries from the Alert table
        Alert.objects.all().delete()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
