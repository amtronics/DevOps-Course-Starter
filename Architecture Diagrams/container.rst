
@startuml Container Diagram
!include <C4/C4_Container>

'LAYOUT_TOP_DOWN()
title Container Diagram for To-Do App

Person(app_user ,"Application User")
System_Boundary(c1, "To-Do App") {
    Container(app_code, "Application Code", "python", "Handles the logic and content creation")
    Container(web_server, "Web Server", "Flask, Gunicorn", "store, process, and deliver requested webpages to the user")
}

System_Ext(trello, "Trello", "stores todo items and their status")

Rel(app_user, web_server, "Uses", "HTTPS")
Rel(web_server, app_code, "Uses", "Python")
Rel_L(app_code, trello, "Reads & Write to", "REST API")

@enduml