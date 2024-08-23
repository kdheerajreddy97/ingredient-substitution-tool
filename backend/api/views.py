from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponseRedirect

substitutes_list = {
    'milk': 'almond milk',
    'egg': 'flaxseed',
    'butter': 'margarine',
    'sugar': 'honey',
    'flour': 'almond flour',
    'yogurt': 'coconut yogurt',
    'cream': 'coconut cream',
    'mayonnaise': 'greek yogurt',
    'sour cream': 'plain yogurt',
    'cheese': 'nutritional yeast',
    'bread crumbs': 'crushed crackers',
    'cornstarch': 'arrowroot powder',
    'soy sauce': 'tamari',
    'lemon juice': 'lime juice',
    'garlic': 'garlic powder',
    'onion': 'onion powder',
    'baking powder': 'baking soda + cream of tartar',
    'vegetable oil': 'coconut oil',
    'heavy cream': 'evaporated milk',
    'buttermilk': 'milk + lemon juice or vinegar',
    'honey': 'maple syrup',
    'vanilla extract': 'almond extract',
    'rice': 'cauliflower rice',
    'pasta': 'zucchini noodles',
    'potato': 'sweet potato',
    'ketchup': 'tomato paste + vinegar + sugar',
    'brown sugar': 'white sugar + molasses',
    'molasses': 'honey',
    'peanut butter': 'almond butter',
    'cocoa powder': 'carob powder',
    'breadcrumbs': 'rolled oats',
    'wine': 'apple cider vinegar',
    'chicken broth': 'vegetable broth',
    'beef': 'mushrooms or lentils',
    'fish sauce': 'soy sauce + lime juice',
    'coconut milk': 'almond milk + coconut extract',
    'cream cheese': 'mascarpone cheese',
    'whipping cream': 'coconut cream',
    'ricotta': 'cottage cheese',
    'brown rice': 'quinoa',
    'applesauce': 'mashed banana',
    'ground beef': 'ground turkey',
    'shortening': 'butter',
    'bread': 'lettuce wraps',
    'tomato sauce': 'tomato paste + water',
    'spaghetti': 'spaghetti squash',
    'pancake syrup': 'maple syrup',
    'croutons': 'toasted nuts or seeds',
    'sour cream': 'cottage cheese + lemon juice',
    'butter': 'coconut oil + salt',
    'heavy cream': 'milk + butter',
    'orange juice': 'lemon juice + sugar',
    'cake flour': 'all-purpose flour + cornstarch',
    'cream of tartar': 'lemon juice or vinegar',
    'self-rising flour': 'all-purpose flour + baking powder + salt',
    'white wine': 'white grape juice + vinegar',
    'soy milk': 'almond milk',
    'half and half': 'milk + butter',
    'apple cider vinegar': 'white vinegar + apple juice',
    'maple syrup': 'agave nectar',
    'allspice': 'cinnamon + cloves + nutmeg',
    'worcestershire sauce': 'soy sauce + vinegar + molasses',
    'parmesan cheese': 'asiago cheese',
    'zucchini': 'eggplant',
    'cream': 'milk + cornstarch',
}


@api_view(['GET'])
def get_substitute(request):
    ingredient = request.GET.get('ingredient')
    if ingredient is None or ingredient.strip() == '':
        return Response({'error': 'No ingredient provided'}, status=400)

    substitute = substitutes_list.get(ingredient.lower(), 'No substitute found')
    return Response({'substitute': substitute})


@api_view(['GET'])
def common_substitutes(request):
    substitutes = [f"{key} -> {value}" for key, value in substitutes_list.items()]
    return Response({'substitutes': substitutes})


@api_view(['POST'])
def submit_substitution(request):
    ingredient = request.data.get('ingredient')
    substitute = request.data.get('substitute')

    if not ingredient or not substitute:
        return Response({'error': 'Both ingredient and substitute are required.'}, status=400)

    ingredient = ingredient.lower().strip()
    substitute = substitute.lower().strip()

    substitutes_list[ingredient] = substitute
    return Response({'message': f'Substitution for {ingredient} added successfully!'})


def redirect_to_api(request):
    return HttpResponseRedirect('/api/')
