
@startuml Container Diagram
!include <C4/C4_Container>

LAYOUT_TOP_DOWN()
title Container Diagram for To-Do App

Person(app_user ,"Application User")
System_Boundary(c1, "To-Do App") {
    Container(web_app, "Web Application", "HTML, Jinja", "Allows users to create new to-do items and mark them as complete/incomplete")
    Container(app_code, "Application Code", "python", "Handles the logic and content creation")
    Container(web_server, "Web Server", "Flask, Gunicorn", "store, process, and deliver requested webpages to the user")
    ContainerDb(db, "Database", "Trello", "Holds to-do items and their 'Done' status")
}

Rel(app_user, web_app, "Uses", "HTTPS")
Rel(web_app, web_server, "served by", "HTTPS")
Rel(web_server, app_code, "started by", "Python")
Rel_L(app_code, db, "Reads & Write to", "REST API")

@enduml