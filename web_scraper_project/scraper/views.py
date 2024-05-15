# scraper/views.py
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from bs4 import BeautifulSoup
import json

def index(request):
    return HttpResponse("Welcome to the Web Scraper!")

@csrf_exempt
def scrape_website(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            website = data.get('website')
            target_element = data.get('target_element')

            if not website or not target_element:
                return JsonResponse({'error': 'Missing website or target_element'}, status=400)

            response = requests.get(website)
            if (response.status_code == 200):
                soup = BeautifulSoup(response.content, 'html.parser')
                target = soup.select_one(target_element)
                if target:
                    scraped_data = target.text.strip()
                    return JsonResponse({'scraped_data': scraped_data})
                else:
                    return JsonResponse({'error': 'Target element not found'}, status=400)
            else:
                return JsonResponse({'error': 'Failed to fetch website'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
