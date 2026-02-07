from fastapi import APIRouter
from typing import List, Dict

router = APIRouter()

# Portfolio data
ABOUT_DATA = {
    "name": "Lilavati Mhaske",
    "title": "MSc Advanced Computer Science Student",
    "university": "University of Leicester",
    "location": "Leicester, United Kingdom",
    "email": "mhaskelilavati4545@gmail.com",
    "phone": "+44 7823708273",
    "intro": "MSc Computer Science student at the University of Leicester with expertise in Backend Engineering, Distributed Systems, and Test Automation.",
    "highlights": [
        {
            "icon": "briefcase",
            "text": "Former QA Engineer at Amazon, improving robotics test automation efficiency by 20%"
        },
        {
            "icon": "trophy",
            "text": "Award winner: ESTECO Software Competition, ASPIRE-2K24, NES Innovation Awards, Student of the Year"
        }
    ],
    "stats": [
        {"icon": "code", "value": "5+", "label": "Major Projects"},
        {"icon": "building", "value": "2", "label": "Internships"},
        {"icon": "trophy", "value": "4", "label": "Awards Won"},
        {"icon": "graduation-cap", "value": "MSc", "label": "Student"}
    ]
}

PROJECTS_DATA = [
    {
        "id": 1,
        "title": "My Shangri-La Referendum (MSLR) Platform",
        "description": "Full-stack voting platform enabling structured digital decision-making through secure referendums and surveys",
        "technologies": ["React", "FastAPI", "MySQL", "REST APIs"],
        "highlights": [
            "Full-stack architecture: React + FastAPI + MySQL",
            "Secure RESTful APIs with validation & logging",
            "Role-based access control & session management"
        ],
        "github": "https://github.com/lilavati-mhaske",
        "category": ["backend", "database", "web", "fullstack"]
    },
    {
        "id": 2,
        "title": "Real-Time Collaborative Whiteboard (Private Cloud)",
        "description": "Distributed real-time collaboration system enabling multiple users to interact concurrently with low-latency synchronization",
        "technologies": ["FastAPI", "Node.js", "Redis", "WebSockets", "AWS", "NGINX", "Prometheus", "Grafana"],
        "highlights": [
            "Redis Pub/Sub + WebSockets: sub-100ms latency for 50+ users",
            "AWS deployment: EC2, VPC, NGINX reverse proxy",
            "Observability: Prometheus, Grafana, CloudWatch",
            "Failure-mode testing: Redis failover, network partitions"
        ],
        "github": "https://github.com/lilavati-mhaske",
        "category": ["distributed", "backend", "cloud", "systems"]
    },
    {
        "id": 3,
        "title": "Amazon Robotics QA Automation",
        "description": "Python-based test automation framework for autonomous robot navigation features in production robotics systems",
        "technologies": ["Python", "unittest", "Simulation Testing", "CI/CD"],
        "highlights": [
            "Python automation: 20% efficiency improvement",
            "Tested VP Docking, Smart Rotation, Obstacle Recovery",
            "Identified 50+ defects through root-cause analysis",
            "Production robotics testing in simulation & CI/CD"
        ],
        "github": "https://github.com/lilavati-mhaske",
        "category": ["automation", "testing", "backend", "systems"]
    },
    {
        "id": 4,
        "title": "River Pollution Detection using Aerial Imagery",
        "description": "Computer vision system using YOLOv8 to detect and quantify polluted regions from drone-captured river imagery",
        "technologies": ["Python", "YOLOv8", "Computer Vision", "PyTorch"],
        "highlights": [
            "YOLOv8 trained on custom aerial imagery dataset",
            "End-to-end ML pipeline: preprocessing to inference",
            "Pollution quantification algorithms for monitoring",
            "Faster detection vs manual inspection methods"
        ],
        "github": "https://github.com/lilavati-mhaske",
        "category": ["ml", "ai", "computer-vision"]
    },
    {
        "id": 5,
        "title": "Professional Portfolio Website",
        "description": "Professional portfolio showcasing projects, skills, and experience with clean UI and responsive design",
        "technologies": ["React", "TypeScript", "FastAPI", "Python"],
        "highlights": [
            "Modern responsive design with dark mode",
            "Smooth animations & interactive features",
            "Performance optimized for fast loading"
        ],
        "github": "https://github.com/Lilavati25/portfolio-website",
        "category": ["web", "frontend", "ui"]
    }
]

EXPERIENCE_DATA = [
    {
        "id": 1,
        "title": "Quality Assurance Engineer Intern",
        "company": "Amazon",
        "duration": "Jan 2024 - Jun 2024",
        "location": "Chennai, India",
        "responsibilities": [
            "Developed and optimised Python-based automation frameworks to test autonomous robotics software, improving test execution efficiency by ~20%",
            "Designed and executed system-level test cases for autonomous navigation, precision movement, obstacle avoidance, and docking behaviours",
            "Conducted regression and exploratory testing to identify edge cases impacting robot navigation, recovery logic, and system reliability in dynamic environments",
            "Analysed inconsistent behaviour across simulation and CI pipeline environments using logs, metrics, and behavioural traces to improve system stability",
            "Designed test scenarios and data collection workflows to validate autonomous recovery mechanisms when navigation paths were obstructed",
            "Collaborated closely with software engineers to debug failures, validate fixes, and improve release reliability by reducing navigation failure rates"
        ]
    },
    {
        "id": 2,
        "title": "Web Developer Intern",
        "company": "NoQs",
        "duration": "July 2023 - Nov 2023",
        "location": "Remote",
        "responsibilities": [
            "Designed and developed responsive, user-facing web applications using HTML, CSS, JavaScript, and React, improving accessibility, usability, and overall user experience",
            "Built and integrated RESTful backend APIs using Node.js and Express, reducing backend response time by ~15% through efficient routing and request handling",
            "Performed end-to-end testing and systematic debugging across frontend and backend components, reducing application errors by ~20%",
            "Collaborated within an Agile development environment, contributing to faster feature delivery, iterative improvements, and improved code quality",
            "Optimised database queries and implemented secure data-handling practices using MongoDB, improving performance for high-traffic scenarios"
        ]
    }
]

SKILLS_DATA = {
    "competencies": [
        {"icon": "💻", "title": "Software Development", "description": "Object-oriented programming, data structures & algorithms, clean code practices"},
        {"icon": "🔧", "title": "Backend Engineering", "description": "Node.js, Express.js, RESTful APIs, HTTP/HTTPS, database design"},
        {"icon": "🌐", "title": "Distributed Systems", "description": "System architecture, scalability, fault tolerance, message queuing"},
        {"icon": "🐛", "title": "Debugging & Reliability", "description": "Test-driven development, system monitoring, performance optimization"}
    ],
    "programming": [
        {"name": "Java", "level": 90},
        {"name": "Python", "level": 90},
        {"name": "JavaScript", "level": 85},
        {"name": "C & C++", "level": 75}
    ],
    "technologies": {
        "Backend & Web": ["Node.js", "Express.js", "FastAPI", "RESTful APIs", "HTTP/HTTPS"],
        "Databases": ["MySQL", "MongoDB", "Oracle", "SQL"],
        "Cloud & Infrastructure": ["AWS (EC2, VPC, S3, Lambda)", "NGINX", "Redis (Pub/Sub)"],
        "Tools & Platforms": ["Git", "GitHub", "Linux", "CI/CD Pipelines", "Prometheus", "Grafana", "Wireshark", "VS Code", "IntelliJ IDEA"]
    }
}

@router.get("/about")
async def get_about():
    """Get about information"""
    return ABOUT_DATA

@router.get("/projects")
async def get_projects():
    """Get all projects"""
    return {"projects": PROJECTS_DATA}

@router.get("/projects/{project_id}")
async def get_project(project_id: int):
    """Get specific project by ID"""
    project = next((p for p in PROJECTS_DATA if p["id"] == project_id), None)
    if project:
        return project
    return {"error": "Project not found"}

@router.get("/experience")
async def get_experience():
    """Get work experience"""
    return {"experience": EXPERIENCE_DATA}

@router.get("/skills")
async def get_skills():
    """Get skills and competencies"""
    return SKILLS_DATA
