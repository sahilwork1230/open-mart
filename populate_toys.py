import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
django.setup()

from shop.models import Category, Product

# Categories to ensure
categories_data = [
    {
        "name": "Shop All",
        "slug": "shop-all",
        "heading": "Our Complete Collection",
        "description": "Discover our full range of amazing toys for all ages.",
        "image": "toys/shop_all.png"
    },
    {
        "name": "New Arrivals",
        "slug": "new-arrivals",
        "heading": "Fresh Fun Just Arrived",
        "description": "Be the first to get the latest and greatest toys.",
        "image": "toys/new_arrival.png"
    },
    {
        "name": "Best Sellers",
        "slug": "best-sellers",
        "heading": "Favored by Families",
        "description": "Our most popular picks that kids love most.",
        "image": "toys/best_seller.png"
    }
]

# Toy products data
toys_data = {
    "shop-all": [
        {"title": "Classic Wooden Train Set", "price": 49.99, "short": "A timeless 50-piece wooden train set.", "long": "High-quality wood, non-toxic paint, and compatible with most major brands."},
        {"title": "Super Action Figure", "price": 24.99, "short": "Articulated hero for epic battles.", "long": "12-inch tall hero with multiple points of articulation and accessories."},
        {"title": "Creative Building Blocks", "price": 34.99, "short": "100 colorful blocks for endless building.", "long": "Eco-friendly materials, various shapes and sizes to spark imagination."},
        {"title": "Soft Plush Teddy Bear", "price": 19.99, "short": "The perfect cuddly companion.", "long": "Extra soft fur, embroidered details, and machine washable."}
    ],
    "new-arrivals": [
        {"title": "Sparky the Robot Dog", "price": 89.99, "short": "Interactive robotic pet with voice commands.", "long": "Responds to touch, voice, and even performs tricks. USB rechargeable."},
        {"title": "Solar System Puzzle", "price": 15.99, "short": "Glow-in-the-dark 200 piece puzzle.", "long": "Educational and fun. Learn about the planets while building."},
        {"title": "Aqua Doodle Mat", "price": 29.99, "short": "Mess-free drawing with water.", "long": "Large mat, disappears as it dries. Perfect for toddlers."},
        {"title": "Junior Chemist Lab", "price": 44.99, "short": "20+ safe experiments for kids.", "long": "Includes real lab equipment and detailed instructions."}
    ],
    "best-sellers": [
        {"title": "Deluxe Dream Dollhouse", "price": 129.99, "short": "3-story dollhouse with elevator.", "long": "Fully furnished with 15 accessories. Fits most 12-inch dolls."},
        {"title": "Ultimate Race Track", "price": 59.99, "short": "Double loop track with motorized booster.", "long": "Gravity-defying stunts and high-speed racing action."},
        {"title": "Magical Castle Tent", "price": 39.99, "short": "Indoor/outdoor pop-up play tent.", "long": "Foldable, portable, and includes star lights for a magical room."},
        {"title": "Magnetic Tiles - 100pc", "price": 69.99, "short": "Strong magnets for building tall structures.", "long": "Transparent colors, 3D shapes, and hours of educational play."}
    ]
}

def populate():
    print("Starting population script...")
    
    # Create or update categories
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            slug=cat_data["slug"],
            defaults={
                "name": cat_data["name"],
                "heading": cat_data["heading"],
                "description": cat_data["description"],
                "category_image": cat_data["image"],
                "is_active": True
            }
        )
        if not created:
            category.name = cat_data["name"]
            category.heading = cat_data["heading"]
            category.description = cat_data["description"]
            category.category_image = cat_data["image"]
            category.save()
            print(f"Updated category: {category.name}")
        else:
            print(f"Created category: {category.name}")

        # Add products to this category
        products_for_cat = toys_data.get(cat_data["slug"], [])
        for p_data in products_for_cat:
            product, p_created = Product.objects.get_or_create(
                title=p_data["title"],
                defaults={
                    "category": category,
                    "name": p_data["title"],
                    "short_description": p_data["short"],
                    "long_description": p_data["long"],
                    "price": p_data["price"],
                    "stock": 50,
                    "is_available": True,
                    "image": cat_data["image"] # Use category image as placeholder for products
                }
            )
            if p_created:
                print(f"  - Created product: {product.title}")
            else:
                product.category = category # Ensure it's in the right category
                product.save()
                print(f"  - Verified product: {product.title}")

    print("Population complete!")

if __name__ == "__main__":
    populate()
