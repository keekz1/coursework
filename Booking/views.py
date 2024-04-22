from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import ToDoList, UnsavedItem, Item, Image
from .forms import CreateNewList, AddMultipleImagesForm
from PIL import Image as PILImage
from io import BytesIO
import os
from django.conf import settings

@login_required
def ind(request, id):
    try:
        ls = ToDoList.objects.get(id=id)
    except ToDoList.DoesNotExist:
        return HttpResponse("ToDoList does not exist.")
    return render(request, "Booking/list.html", {"ls": ls})

@login_required
def home(request):
    user = request.user
    return render(request, 'home.html', {'user': user})

@login_required
def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            return HttpResponseRedirect(f"/{t.id}")
    else:
        form = CreateNewList()
    return render(request, "create.html", {"form": form})

def handle_temporary_image_upload(image, itemDes, folder):
    img = PILImage.open(image)
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Create a BytesIO object to store the image data
    img_io = BytesIO()
    img.save(img_io, format='JPEG')

    # Generate a unique filename using the itemDes
    file_name = itemDes.replace(" ", "_").lower()  # Use itemDes to generate file name

    # Define the directory to save temporary images
    temp_upload_path = os.path.join(settings.MEDIA_ROOT, folder)
    os.makedirs(temp_upload_path, exist_ok=True)

    # Save the image with a unique filename
    temp_image_path = os.path.join(temp_upload_path, f'{file_name}.jpg')
    with open(temp_image_path, 'wb') as file:
        file.write(img_io.getvalue())

    # Return the relative URL of the uploaded image
    return os.path.relpath(temp_image_path, settings.MEDIA_ROOT)

@login_required
@staff_member_required
def list_view(request, id):
    try:
        ls = ToDoList.objects.get(id=id)
    except ToDoList.DoesNotExist:
        return HttpResponse("ToDoList does not exist.")

    unsaved_items = UnsavedItem.objects.all()

    if request.method == 'POST':
        if 'add_item' in request.POST:
            itemDes = request.POST.get('new_item_itemDes')
            image = request.FILES.get('item_image')  # Get uploaded image
            if itemDes:
                if image:
                    # Save unsaved item to the database
                    UnsavedItem.objects.create(itemDes=itemDes, image=image)
                else:
                    UnsavedItem.objects.create(itemDes=itemDes)
        elif 'save' in request.POST:
            # Move unsaved items to saved items
            for unsaved_item in unsaved_items:
                itemDes = unsaved_item.itemDes
                image = unsaved_item.image
                # Save the unsaved item to the main database
                if image:  # Check if there's an image associated with the unsaved item
                    saved_item = Item.objects.create(lists=ls, itemDes=itemDes)
                    Image.objects.create(item=saved_item, image=image)
            # Clear unsaved items from the database
            UnsavedItem.objects.all().delete()
            # Redirect to the same page after saving
            return redirect('list_view', id=id)
        elif 'delete_item' in request.POST:
            item_id = request.POST.get('delete_item')
            ls.item_set.filter(id=item_id).delete()
            # Redirect to the same page after deletion
            return redirect('list_view', id=id)

    # Retrieve saved items
    saved_items = ls.item_set.all()

<<<<<<< HEAD
    return render(request, "Booking/list.html", {"ls": ls, "unsaved_items": unsaved_items, "saved_items": saved_items})

@login_required
@staff_member_required
def add_multiple_images_view(request):
    if request.method == 'POST':
        form = AddMultipleImagesForm(request.POST, request.FILES)
        if form.is_valid():
            # Logic to handle multiple images
            # Retrieve the item ID from the form
            item_id = form.cleaned_data['item_id']
            # Retrieve the images from the form
            images = request.FILES.getlist('images')
            for image in images:
                # Save each image to the database
                item = Item.objects.get(id=item_id)
                Image.objects.create(item=item, image=image)
            return redirect('list_view', id=item_id)  # Redirect to the list view page after adding images
    else:
        form = AddMultipleImagesForm()
    return render(request, "Booking/add_multiple_images.html", {"form": form})
from django.http import JsonResponse



def delete_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('itemId')  # Get the item ID from the POST request
        try:
            # Try to retrieve the item from the Item model
            item = Item.objects.get(id=item_id)
            item.delete()  # Delete the item from the database
            return JsonResponse({'success': True})  # Return a success response
        except Item.DoesNotExist:
            try:
                # Try to retrieve the item from the UnsavedItem model
                unsaved_item = UnsavedItem.objects.get(id=item_id)
                unsaved_item.delete()  # Delete the unsaved item
                return JsonResponse({'success': True})  # Return a success response
            except UnsavedItem.DoesNotExist:
                # If neither saved nor unsaved item is found, return an error response
                return JsonResponse({'success': False, 'error': 'Item not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})  # Return an error response for invalid request method
=======
    return render(request, "main/list.html", {"ls": ls, "unsaved_items": unsaved_items, "saved_items": saved_items})

def Search_Engine(request):
    if request.method == "POST":
        searched = request.POST['searched']
        items = Item.objects.filter( text = searched)

        return render(request,
        'Search_Engine.html', 
        {'searched':searched,'user':items})
    else:
        return render(request,
        'Search_Engine.html', 
        {})
>>>>>>> e02c072fbd14da945f6127def07210df43e7a399
