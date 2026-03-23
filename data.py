# ============================================================
# Portfolio Data - Edita este archivo para personalizar tu sitio
# ============================================================

portfolio_data = {
    # --- Información personal ---
    "name": "Manuel Rivera",
    "greeting": "Hola, soy",
    "greeting_en": "Hi, I'm",
    "role": "Software Engineer",
    "role_en": "Software Engineer",
    "tagline": "Soy un ingeniero de software especializado en desarrollo web. "
               "Mi pasión es mejorar la experiencia de desarrollo creando "
               "herramientas que optimizan los flujos de trabajo.",
    "tagline_en": "I'm a software engineer focused on web development. "
               "I enjoy improving developer experience by building tools that streamline workflows.",
    "portrait": "/static/img/Manu-pixel.png",
    "timezone": "UTC-6",
    "location": "El Salvador",

    # --- Navegación ---
    "nav_links": [
        {"label": "Proyectos", "label_en": "Projects", "href": "#proyectos", "i18n": "nav.projects"},
        {"label": "Experiencia", "label_en": "Experience", "href": "#work", "i18n": "nav.experience"},
        {"label": "Contacto", "label_en": "Contact", "href": "#connect", "i18n": "nav.contact"},
    ],

    # --- Proyectos ---
    "proyectos_intro": "Aquí verás mis proyectos: herramientas, librerías y demos desarrollados por mí.",
    "proyectos_intro_en": "Here you'll find my projects: tools, libraries and demos I've built.",
    "github_username": "Manriv31",
    "projects": [
        {
            "name": "Sistema Integral de Contratos y Pagos - SICP",
            "name_en": "Integrated Contracts and Payments System - SICP",
            "description": "Sistema de gestión de contratos y pagos para uso interno de Banco Agricola, desarrollado con Python y Flask. Permite la administración eficiente de proveedores, contratos, seguimiento de pagos y generación de reportes.",
            "description_en": "Contract and payments management system for internal use at Banco Agrícola, built with Python and Flask. Enables efficient vendor, contract, payment tracking and reporting.",
            "image": "/static/img/projects/sicp.svg",
            "images": ["/static/img/projects/sicp.svg", "/static/img/projects/sicp.svg"],
            "stack": ["Python", "Flask", "SQLAlchemy"],
            "language": "Python",
        },
        {
            "name": "Sitio Web - Akira",
            "name_en": "Website - Akira",
            "description": "Catalogo de productos para una marca de velas aromaticas, este consiste en un apartado donde se muestran los productos con sus caracteristicas, carrito de compras, registro de usuarios, ordenes de productos por usuario y un panel de administrador para gestionar los productos, ordenes y usuarios, desarrollado con Python, Flask y SQLAlchemy.",
            "description_en": "Product catalog site for a scented-candles brand. Shows product pages, cart, user accounts, orders per user and an admin panel to manage products, orders and users. Built with Python, Flask and SQLAlchemy.",
            "image": "/static/img/projects/akira.svg",
            "images": ["/static/img/projects/akira.svg", "/static/img/projects/akira.svg"],
            "stack": ["Python", "Flask", "SQLAlchemy", "Bootstrap"],
            "language": "Python",
        },
        {
            "name": "Portafolio Personal",
            "name_en": "Personal Portfolio",
            "description": "Mi portafolio personal, construido con python y flask, utilizando un diseño moderno y responsivo para mostrar mis proyectos, experiencia laboral y enlaces de contacto.",
            "description_en": "My personal portfolio, built with Python and Flask, using a modern responsive design to showcase projects, work experience and contact links.",
            "image": "/static/img/projects/portafolio.svg",
            "images": ["/static/img/projects/portafolio.svg", "/static/img/projects/portafolio.svg"],
            "stack": ["Python", "Flask", "HTML", "CSS"],
            "language": "Python"
        },
        {
            "name": "BlogPosts",
            "name_en": "BlogPosts",
            "description": "Sitio web de blog personal, desarrollado con Python y Flask, que permite publicar artículos, categorizar contenido y gestionar comentarios. El sitio cuenta con un diseño limpio y funcional para una experiencia de lectura agradable.",
            "description_en": "Personal blog site developed with Python and Flask, enabling article publishing, content categorization and comment management. Clean, readable design.",
            "image": "/static/img/projects/blogposts.svg",
            "images": ["/static/img/projects/blogposts.svg", "/static/img/projects/blogposts.svg"],
            "stack": ["Python", "Flask"],
            "language": "Python",
        },
        {
            "name": "SisPro",
            "name_en": "SisPro",
            "description": "Aplicativo web interno para la unificacion de estadisticas de institucion gobernamental, deesarrollado con PHP y CakePHP que permite la recopilación, análisis y visualización de datos estadísticos provenientes de diversas fuentes.",
            "description_en": "Internal web application for unifying statistics at a government institution, developed with PHP and CakePHP to collect, analyze and visualize statistical data from various sources.",
            "image": "/static/img/projects/sispro.svg",
            "images": ["/static/img/projects/sispro.svg", "/static/img/projects/sispro.svg"],
            "stack": ["PHP", "CakePHP", "MySQL"],
            "language": "PHP",
        },
        {
            "name": "BusitoSV",
            "name_en": "BusitoSV",
            "description": "Aplicativo web como proyecto de tesis universitaria para la gestión de rutas y horarios de transporte público en El Salvador, desarrollado con PHP y Laravel. Permite a los usuarios consultar rutas por medio de un mapa interactivo, visualizar horarios posibles de llegada y salida.",
            "description_en": "Web application (thesis project) for managing public transport routes and schedules in El Salvador, developed with PHP and Laravel. Users can query routes on an interactive map and view possible arrival/departure times.",
            "image": "/static/img/projects/busitosv.svg",
            "images": ["/static/img/projects/busitosv.svg", "/static/img/projects/busitosv.svg"],
            "stack": ["PHP", "Laravel", "JavaScript"],
            "language": "PHP",
        },
        # {
        #     "name": "Proyecto Zeta",
        #     "description": "Linter personalizado para mantener calidad en el código.",
        #     "url": "https://github.com/tu-usuario/proyecto-zeta",
        #     "language": "Python",
        #     "stars": 180,
        #     "downloads": "5K/mes",
        # },
    ],

    # --- Experiencia laboral ---
    "work": {
        "current_role": "Observability & Data Analyst",
        "company": "Banco Agricola",
        "company_url": "https://www.bancoagricola.com/",
        "description": "Soy responsable de implementar puntos de monitoreo en aplicaciones y sistemas críticos, "
               "aplicando la metodología de observabilidad de cinco capas para garantizar alta disponibilidad "
               "y detección temprana de anomalías. Además desarrollo y mantengo pipelines ETL en Python para "
               "extraer y transformar métricas de negocio, y construyo herramientas internas que automatizan "
               "procesos, mejoran la operativa del equipo y facilitan la respuesta a incidentes. También desarrollo "
               "aplicaciones web internas para el área, creando herramientas que soportan los flujos de trabajo "
               "y la operativa diaria.",
        "description_en": "I am responsible for implementing monitoring points in critical applications and systems, "
            "applying a five-layer observability methodology to ensure high availability and early anomaly detection. "
            "I also develop and maintain ETL pipelines in Python to extract and transform business metrics, and build "
            "internal tools that automate processes, improve team operations and facilitate incident response. "
            "Additionally, I develop internal web applications to support daily workflows.",
        "previous": "Anteriormente, trabajé en desarrollador Fullstack,"
                "en la que participé en el desarrollo de una aplicacion web" 
                "para realizar tareas tediosas en una forma mas optimizada y eficiente.",
        "previous_en": "Previously, I worked as a Fullstack developer where I participated in building a web application "
                "that automated tedious tasks to improve efficiency and workflows.",
        "cv_url": "#",
    },

    # --- Experiencia detallada (página dedicada) ---
    "experience_intro": "Soy un ingeniero de software especializado en observabilidad y desarrollo back-end, centrado en crear soluciones internas que mejoren la operativa del equipo.",
    "experience_intro_en": "I'm a software engineer focused on observability and back-end development, building internal solutions that improve team operations.",

    "detailed_experience": [
        {
            "title": "Analista de Observabilidad y Datos",
            "title_en": "Observability & Data Analyst",
            "company": "OE International - Banco Agricola",
            "company_en": "OE International - Banco Agricola",
            "period": "2021 - Actualidad",
            "period_en": "2021 - Present",
            "location": "San Salvador, El Salvador",
            "location_en": "San Salvador, El Salvador",
            "summary": "Responsable de implementar puntos de monitoreo en las aplicaciones y sistemas críticos de Banco Agrícola, aplicando la metodología de observabilidad de cinco capas para garantizar alta disponibilidad, detección temprana de anomalías y continuidad operativa. Realicé análisis de datos diseñando y manteniendo pipelines ETL en Python para extraer, transformar y entregar métricas de negocio significativas, permitiendo a las partes interesadas tomar decisiones informadas basadas en datos en tiempo real e históricos. Complementé las responsabilidades de monitoreo y analítica con desarrollo de software interno, creando herramientas web y soluciones de automatización que mejoraron la eficiencia del equipo y estandarizaron los flujos de trabajo operativos.",

            "summary_en": "Responsible for implementing monitoring checkpoints across Banco Agricola's critical applications and systems, applying the five-layer observability methodology to ensure high availability, early anomaly detection, and operational continuity. Performed data analysis by designing and maintaining ETL pipelines with Python to extract, transform, and deliver meaningful business metrics, enabling stakeholders to make informed decisions based on real-time and historical data. Complemented monitoring and analytics responsibilities with internal software development, building web-based tools and automation solutions that improved team efficiency and standardized operational workflows.",
            "highlights": [
                "Desempeñé un papel clave en la identificación y mitigación de riesgos operativos, contribuyendo a la estabilidad financiera y la seguridad de la institución.",
                "Colaboré con equipos multifuncionales para desarrollar y mejorar los protocolos de respuesta a incidentes, asegurando una respuesta rápida y eficaz ante anomalías detectadas.",
                "Lideré iniciativas internas como la programación y orquestación de ETL en servidor, el despliegue de un repositorio interno en Gitea, la implementación de una wiki interna con Bookstack y la configuración de alertas eficientes mediante webhooks de las herramientas de monitoreo integrados con Microsoft Teams.",
                "Desarrollé sistemas web internos en Python (Flask, Django), aplicando prácticas de codificación segura.",
            ],
            "highlights_en": [
                "Played a key role in identifying and mitigating operational risks, contributing to the financial stability and security of the institution.",
                "Collaborated with cross-functional teams to develop and improve incident response protocols, ensuring rapid and effective response to detected anomalies.",
                "Led internal initiatives including ETL scheduling and orchestration on server, deployment of an internal Gitea repository, implementation of an internal Bookstack wiki, and configuration of efficient alerting through monitoring tool webhooks integrated with Microsoft Teams.",
                "Built internal web systems using Python with Flask and Django, applying secure coding practices.",
            ],
            "stack": ["Python", "Flask", "Django", "Docker", "GitHub", "Dynatrace", "Zabbix", "Grafana", "PostgreSQL", "Linux", "MySQL", "FastAPI"],
        },
        {
            "title": "Desarrollador Full Stack",
            "title_en": "Full Stack Developer",
            "company": "Fosalud",
            "company_en": "Fosalud",
            "period": "2020 - 2021",
            "period_en": "2020 - 2021",
            "location": "San Salvador, El Salvador",
            "location_en": "San Salvador, El Salvador",
            "summary": "Lideré el desarrollo y despliegue de un sistema web para gestionar estadísticas e indicadores clave de programas de salud, construido con PHP (CakePHP), MySQL, JavaScript (jQuery) y CSS, con ZingChart para visualización de datos. Me encargué del análisis de requerimientos, diseño de arquitectura, desarrollo de funcionalidades, pruebas y documentación del proyecto.",
            "summary_en": "Led the development and deployment of a web-based system to manage health program statistics and key indicators, built with PHP (CakePHP), MySQL, JavaScript (jQuery), and CSS, with ZingChart for data visualization. Handled requirements analysis, architecture design, feature development, testing, and project documentation.",
            "highlights": [
                "Entregué un sistema en producción actualmente en uso por el equipo de captura de datos de Fosalud, unificando la información y permitiendo la generación eficiente de reportes.",
                "Automatización de procesos manuales, agilizando tareas diarias y mejorando la calidad de los datos en todo el equipo.",
            ],
            "highlights_en": [
                "Delivered a production system currently in use by Fosalud's data entry team, unifying information and enabling efficient report generation.",
                "Automated manual processes, streamlining daily tasks and improving data quality across the team.",
            ],
            "stack": ["PHP", "CakePHP", "MySQL", "JavaScript", "jQuery", "CSS", "ZingChart"],
        },
        {
            "title": "Analista QA",
            "title_en": "QA Analyst",
            "company": "Grupo Satelite",
            "company_en": "Grupo Satelite",
            "period": "2019 - 2020",
            "period_en": "2019 - 2020",
            "location": "San Salvador, El Salvador",
            "location_en": "San Salvador, El Salvador",
            "summary": "Realicé pruebas de aseguramiento de calidad en el software ERP de la empresa, enfocándome en la gestión de usuarios/roles y administración de inventarios. Llevé a cabo pruebas manuales detalladas y en tiempo real para garantizar la funcionalidad del sistema, documentando los problemas encontrados y colaborando con el equipo de desarrollo para su resolución.",
            "summary_en": "Performed comprehensive QA testing on ERP software, focusing on user/role management and inventory administration. Conducted detailed manual and real-time testing to ensure system functionality, documenting issues and collaborating with the development team for resolution.",
            "highlights": [
                "Contribuí a scripts de pruebas automatizadas que mejoraron la eficiencia del proceso de QA.",
                "Integré enfoques de pruebas manuales y automatizadas para una garantía de calidad más efectiva.",
                "Trabajé con clientes de alto perfil incluyendo Centro Cultural Salvadoreño, Pricesmart y Save the Children.",
            ],
            "highlights_en": [
                "Contributed to automated testing scripts that improved the efficiency of the QA process.",
                "Integrated manual and automated testing approaches for more effective quality assurance.",
                "Worked with high-profile clients including Centro Cultural Salvadoreño, Pricesmart, and Save the Children.",
            ],
            "stack": ["Python", "JavaScript", "Selenium", "SQL", "Manual Testing", "Automated Testing"],
        },
        {
            "title": "Desarrollador Web",
            "title_en": "Web Developer",
            "company": "Brightness Developing Solutions - Fast Care",
            "company_en": "Brightness Developing Solutions - Fast Care",
            "period": "2019 - 2019",
            "period_en": "2019 - 2019",
            "location": "San Salvador, El Salvador",
            "location_en": "San Salvador, El Salvador",
            "summary": "Desarrollé y mantuve aplicaciones web en PHP para la gestión de inventarios de suministros médicos. Diseñé y optimicé bases de datos MySQL para mejorar el rendimiento de las consultas y la eficiencia del almacenamiento de datos. Colaboré con el equipo de desarrollo para implementar nuevas funcionalidades alineadas con los requerimientos del negocio.",
            "summary_en": "Developed and maintained PHP web applications for medical supply inventory management. Designed and optimized MySQL databases to improve query performance and data storage efficiency. Collaborated with the development team to implement new features aligned with business requirements.",
            "highlights": [
                "Construí sistemas robustos de gestión de inventarios asegurando un seguimiento confiable de los suministros médicos.",
                "Optimicé consultas de bases de datos, mejorando la velocidad de la aplicación y el rendimiento general.",
                "Proporcioné soporte técnico, identificando cuellos de botella y depurando problemas para mantener la calidad del software.",
            ],
            "highlights_en": [
                "Built robust inventory management systems ensuring reliable tracking of medical supplies.",
                "Optimized database queries, improving application speed and overall performance.",
                "Provided technical support, identifying bottlenecks and debugging issues to maintain software quality.",
            ],
            "stack": ["PHP", "JavaScript", "CSS", "SQL"],
        },
    ],

    # --- Consultoría ---
    "freelance": {
        "enabled": True,
        "description": "Ofrezco servicios freelance enfocados en desarrollo web, análisis de datos y optimización de procesos. "
            "Trabajo por proyecto o por contrato para mejorar flujos de trabajo y entregar soluciones reutilizables.",
        "description_en": "I offer freelance services focused on web development, data analysis and process optimization. "
            "I work on a project or contract basis to improve workflows and deliver reusable solutions.",
        "specialties": [
            "Desarrollo web",
            "Análisis de datos",
            "Automatización",
            "Observabilidad",
        ],
        "specialties_en": [
            "Web development",
            "Data analysis",
            "Automation",
            "Observability",
        ],
    },

    # --- Section titles and misc translations ---
    "freelance_title": "Servicios freelance",
    "freelance_title_en": "Freelance Services",

    "connect_title": "Conectemos",
    "connect_title_en": "Let's connect",

    "connect_description": "¡Siéntete libre de conectar conmigo en cualquiera de estas plataformas!",
    "connect_description_en": "Feel free to connect with me on any of these platforms!",

    "cv_link_text": "Leer mi CV →",
    "cv_link_text_en": "Read my CV →",

    "footer_suffix": "Hecho con Python & Flask",
    "footer_suffix_en": "Made with Python & Flask",

    # --- Redes sociales ---
    "social_links": [
        {
            "platform": "GitHub",
            "handle": "@Manriv31",
            "url": "https://github.com/Manriv31",
            "icon": "github",
        },
        {
            "platform": "X / Twitter",
            "handle": "@Manriv31",
            "url": "https://x.com/Manriv31",
            "icon": "twitter",
        },
        {
            "platform": "LinkedIn",
            "handle": "manriv31",
            "url": "https://linkedin.com/in/manriv31",
            "icon": "linkedin",
        },
        {
            "platform": "Email",
            "handle": "manrivargueta@gmail.com",
            "url": "mailto:manrivargueta@gmail.com",
            "icon": "email",
        },
    ],

    # --- Links adicionales ---
    "additional_links": [
        {"label": "Blog", "label_en": "Blog", "url": "#"}
    ],
}
