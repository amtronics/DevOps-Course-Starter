@startuml Component Diagram
!include <C4/C4_Container>
!include <C4/C4_Component>

LAYOUT_TOP_DOWN()
title Component Diagram for To-Do App - Application Code

Container_Boundary(c1, "Application Code") {
    Component(trello, "Trello Handler Component", "Python", "Uses lists/cards in trello for storing todo items")
    Component(web_app, "Web App Component", "python", "Creates the pages user interacts with")
    Component(flask, "Flask Webserver Component", "Docker, Flask", "handles creations of dev image and launching webserver")
    Component(gunicorn, "Gunicorn Webserver Component", "Docker, Gunicorn", "handles creations of prod image and launching webserver")
}
ContainerDb(db, "Database", "Trello", "Holds to-do items and their 'Done' status")
Component(prod_web_server, "Production Web Server", "Gunicorn", "store, process, and deliver requested webpages to the user")
Component(dev_web_server, "Development Web Server", "Flask", "store, process, and deliver requested webpages to the user")

Rel_R(trello, db, "Reads & Write to", "REST API")
Rel(gunicorn, web_app, "Uses", "python")
Rel(flask, web_app, "Uses", "python")

Rel(prod_web_server, gunicorn, "started by", "python")
Rel(dev_web_server, flask, "started by", "python")

@enduml