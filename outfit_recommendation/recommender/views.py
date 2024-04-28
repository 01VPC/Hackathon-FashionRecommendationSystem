from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Outfit
import joblib
import pandas as pd
from .models import FashionItem
from .fashion_recommender import FashionRecommender

def recommend_items(request):
    if request.method == 'POST':
        gender = request.POST['gender']
        MasterCategory = request.POST['MasterCategory']
        SubCategory = request.POST['SubCategory']
        articletype = request.POST['articletype']
        usage = request.POST['usage']
        colour = request.POST['colour']
    input_categories = [ gender, MasterCategory, SubCategory, articletype, usage, colour]
    fashion_data = FashionItem.objects.all().values()  # Assuming you have a model named FashionItem
    df = pd.DataFrame(list(fashion_data))
    

    recommender = FashionRecommender(item_features=None)  # Pass None initially
    recommendations = recommender.recommend_items(input_categories, df)

    return render(request, 'recommendations.html', {'recommendations': recommendations})
def recommend_outfit(request):
    if request.method == 'POST':
        form = request.POST
        gender = request.POST['gender']
        MasterCategory = request.POST['mastercategory']
        SubCategory = request.POST['subcategory']
        articletype = request.POST['articletype']
        usage = request.POST['usage']
        colour = request.POST['colour']

        vectorizer = joblib.load(r"C:\Users\Vaishnavi\Desktop\Final_hackathon\outfit_recommendation\recommender\savedModels\vectorizer.joblib")
        input_features = ' '.join([gender, MasterCategory, SubCategory, articletype, usage, colour])
        
        # Assuming FashionRecommender returns a list of image paths
        recommender = FashionRecommender(item_features=None)  # Pass None initially
        recommended_outfit = recommender.recommend_outfit([input_features])

        # Pass the recommended outfit image paths to the template
        return render(request, 'recommendation.html', {'outfit_images': recommended_outfit})
    else:
        return render(request, 'input_form.html')