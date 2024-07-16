from django.shortcuts import render

# Create your views here.
def Courses(request):
    AllCourses = [
    {
        "course_id": 1,
        "course_poster":"https://placehold.co/600x400",
        "course_name": "Introduction to Physics",
        "course_duration": 4,
        "course_price": 150,
        "course_description": "Explore the fundamental principles of classical and modern physics.",
        "course_instructor": "Dr. Emily Newton",
        "course_reviews": 12,
        "course_rating": 4.7,
        "isPaid": True    
    },
    {
        "course_id": 2,
        "course_poster":"https://placehold.co/600x400",
        "course_name": "Organic Chemistry Fundamentals",
        "course_duration": 5,
        "course_price": 180,
        "course_description": "Learn the basics of organic compounds and their reactions.",
        "course_instructor": "Prof. Michael Carbon",
        "course_reviews": 8,
        "course_rating": 4.5,
        "isPaid": True
    },
    {
        "course_id": 3,
        "course_poster":"https://placehold.co/600x400",
        "course_name": "Cellular Biology",
        "course_duration": 4,
        "course_price": 160,
        "course_description": "Dive into the structure and function of cells, the building blocks of life.",
        "course_instructor": "Dr. Sarah Genome",
        "course_reviews": 15,
        "course_rating": 4.8,
        "isPaid": True
    },
    {
        "course_id": 4,
        "course_poster":"https://placehold.co/600x400",
        "course_name": "Environmental Science",
        "course_duration": 3,
        "course_price": 130,
        "course_description": "Understand the interactions between human society and the natural world.",
        "course_instructor": "Prof. David Eco",
        "course_reviews": 10,
        "course_rating": 4.6,
        "isPaid": True
    },
    {
        "course_id": 5,
        "course_poster":"https://placehold.co/600x400",
        "course_name": "Astronomy: Exploring the Universe",
        "course_duration": 4,
        "course_price": 170,
        "course_description": "Journey through the cosmos and learn about celestial bodies and phenomena.",
        "course_instructor": "Dr. Stella Nova",
        "course_reviews": 14,
        "course_rating": 4.9,
        "isPaid": True
    },
    {
        "course_id": 6,
        "course_poster":"https://placehold.co/600x400",
        "course_name": "Neuroscience Basics",
        "course_duration": 5,
        "course_price": 190,
        "course_description": "Explore the structure and function of the nervous system and the brain.",
        "course_instructor": "Prof. Alex Neuron",
        "course_reviews": 9,
        "course_rating": 4.7,
        "isPaid": True
    },
    {
        "course_id": 7,
        "course_poster":"https://placehold.co/600x400",
        "course_name": "Quantum Mechanics",
        "course_duration": 6,
        "course_price": 220,
        "course_description": "Delve into the bizarre world of quantum physics and its applications.",
        "course_instructor": "Dr. Quentin Wave",
        "course_reviews": 7,
        "course_rating": 4.8,
        "isPaid": True
    },
    {
        "course_id": 8,
        "course_poster":"https://placehold.co/600x400",
        "course_name": "Genetics and Heredity",
        "course_duration": 4,
        "course_price": 160,
        "course_description": "Understand how traits are passed from one generation to the next.",
        "course_instructor": "Prof. Helix DNA",
        "course_reviews": 11,
        "course_rating": 4.6,
        "isPaid": True
    },
    {
        "course_id": 9,
        "course_poster":"https://placehold.co/600x400",
        "course_name": "Meteorology: Weather and Climate",
        "course_duration": 3,
        "course_price": 140,
        "course_description": "Learn about atmospheric phenomena and global climate patterns.",
        "course_instructor": "Dr. Cloudy Skies",
        "course_reviews": 8,
        "course_rating": 4.5,
        "isPaid": True
    },
    {
        "course_id": 10,
        "course_poster":"https://placehold.co/600x400",
        "course_name": "Biochemistry",
        "course_duration": 5,
        "course_price": 200,
        "course_description": "Study the chemical processes within and related to living organisms.",
        "course_instructor": "Prof. Enzyme Reaction",
        "course_reviews": 13,
        "course_rating": 4.7,
        "isPaid": True
    },
    {
        "course_id": 11,
        "course_poster":"https://placehold.co/600x400",
        "course_name": "Marine Biology",
        "course_duration": 4,
        "course_price": 170,
        "course_description": "Explore the diverse life forms in the world's oceans and their ecosystems.",
        "course_instructor": "Dr. Coral Reef",
        "course_reviews": 9,
        "course_rating": 4.8,
        "isPaid": True
    }
]
    
    return render(request, "Course.html",{"AllCourses": AllCourses})