from django.shortcuts import render
from .models import *
import requests
from .forms import *
from pprint import pprint
from random import randint
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from math import ceil
import os
import xmltodict
import json
from django.core.paginator import Paginator
from test_task.settings import DB_POPULATION_PERIOD
from datetime import datetime, timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Q

class Main:
    def homepage(request):

        now = datetime.now(timezone.utc)

        last_program_change = max([i.updated_at for i in Program.objects.all()])
        last_product_change = max([i.updated_at for i in Product.objects.all()])

        progr_time_diff = now-last_program_change
        product_time_diff = now-last_product_change

        print("\n Секунд до автоматического обновления БД: {}\n".format((DB_POPULATION_PERIOD - max(product_time_diff,progr_time_diff).total_seconds())))

        progr_num = round(int(float(str(progr_time_diff.total_seconds() * 1000)))/1000,0)
        product_num = round(int(float(str(product_time_diff.total_seconds() * 1000)))/1000,0)


        no_progr_changes = int(progr_num)
        no_product_changes = int(product_num)

        print("Время с посленденго обновления магазинов: ", no_progr_changes)
        print("Время с посленденго обновления продуктов: ", no_product_changes, "\n")

        if no_progr_changes >= DB_POPULATION_PERIOD:
            return redirect("populate_shops")

        if no_product_changes >= DB_POPULATION_PERIOD:
            return redirect("populate_products")

        return render(request, "general/homepage.html", {})



    def api_test(request):
        ctx = {}
        return render(request, "api_test.html",ctx)

    def rest_categories(request):
        pages =[i+1 for i in range(int(ceil(Category.objects.all().count()/10)))]
        ctx = {
        "pages":pages,
        }
        return render(request, "general/rest_categories.html",ctx)


    def rest_service(request):
        pages =[i+1 for i in range(int(ceil(Program.objects.all().count()/10)))]
        ctx = {
        "pages":pages,
        }
        return render(request, "general/rest_service.html",ctx)


    @login_required(login_url='/login_view')
    def custom_admin(request):
        categories = Category.objects.all()
        ctx = {
        "categories":categories,
        }
        return render(request, "general/custom_admin.html", ctx)


    def login_view(request):
        form = UserLoginForm(request.POST or None)
        ctx = {"form":form}
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request,username = username, password = password)
            if user is None:
                messages.add_message(request,messages.INFO,"Неверный логин и/или пароль")
                return render(request,"login_view.html",ctx)
            else:
                login(request,user)
                return redirect("custom_admin")

        return render(request,"login_view.html",ctx)



    @login_required(login_url='/login_view')
    def edit_category(request,pk):
        if request.method == "POST":
            old_category = Category.objects.get(id=pk)
            form = CategoryModelForm(request.POST, request.FILES, instance = old_category)

            print(form.is_valid())
            if form.is_valid():
                image_path = old_category.image.path
                if os.path.exists(image_path):
                    os.remove(image_path)
                form.save()
                return redirect('custom_admin')
        else:
            category = Category.objects.get(id=pk)
            category_model_form = CategoryModelForm(instance = category)
            ctx = {
            "category": category,
            "category_model_form":category_model_form,
            "pk" : category.pk,
            }
            return render(request, "general/edit_category.html", ctx)


    def search(request, page_num=1, search_string_pag = None):
        if search_string_pag == "None":
            search_string_pag = None

        search_string= request.GET.get('search_string')

        if search_string is not None:
            page_num = 1

        if search_string_pag is not None:
            search_string = search_string_pag

        res = ""
        if search_string is not None:
            res = Product.objects.filter(
                Q(name__icontains=search_string) | Q(model__icontains=search_string)
            )

        else:
            res = Product.objects.all()


        search_string= request.GET.get('search_string')
        try:
            if search_string_pag != search_string:
                res = Product.objects.filter(
                    Q(name__icontains=search_string) | Q(model__icontains=search_string)
                )
        except: pass
        p = Paginator(res,10)
        page_obj = p.get_page(page_num)

        if request.GET.get('search_string') is None:
            search_string = search_string_pag

        ctx = {
        "page_obj":page_obj,
        "search_string":search_string,
        }
        return render(request, "general/search.html",ctx)


    def populate_shops(request):
        access_token = "Bearer SotGfyXnYgCnNvSgpszeAaXRHnjLvN" # 7 days
        link = "https://api.admitad.com/advcampaigns/website/2090016/?limit=50"
        result = requests.get(link, headers={'Authorization': 'Bearer SotGfyXnYgCnNvSgpszeAaXRHnjLvN'})
        data = result.json()
        programs = data["results"]

        pr_ctgrs = []
        for program in programs:
            for category in program["categories"]:
                ctg, created = Category.objects.get_or_create(name = category["name"])
                pr_ctgrs.append(ctg)

            pr, created = Program.objects.get_or_create(name = program["name"])

            for pr_ctg in pr_ctgrs:
                pr.category.add(pr_ctg)
            pr.actions_detail = program["actions_detail"][0]["name"]
            pr.image = program["image"]
            pr.gotolink = program["gotolink"]
            pr.products_xml_link = program["products_xml_link"]
            pr.save()
            pr_ctgrs.clear()
            print(pr)

        ctx = {
        "state":"БД магазинов успешно обновлена"
        }
        return render(request, "general/homepage.html", ctx)



    def populate_products(request):

        link = "http://export.admitad.com/webmaster/websites/2090016/products/export_adv_products/?user=shaa80&code=nztwz8ig83&feed_id=22196&format=xml"
        response = requests.get(link)

        d = xmltodict.parse(response.content)
        products = d["yml_catalog"]["shop"]["offers"]["offer"]
        for product in products:
            p, created = Product.objects.get_or_create(name = product["name"], model = product["model"])
            p.price = float(product["price"])
            try:
                p.image = product["picture"][0]
            except: pass
            p.url = product["url"]
            print(p)
            p.save()


        ctx = {
        "state":"БД товаров успешно обновлена"
        }
        return render(request, "general/homepage.html", ctx)
