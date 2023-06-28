@startuml Component Diagram
!include <C4/C4_Container>
!include <C4/C4_Component>

LAYOUT_TOP_DOWN()
title Component Diagram for To-Do App - Application Code


Container_Boundary(c1, "Application Code") {
    Component(trello_comp, "Trello Component", "Python", "Uses lists/cards in trello for storing todo items")
    Component(gunicorn, "Gunicorn Component", "Gunicorn", "WSGI")
    Component(flask, "Flask App", "python", "Creates the pages user interacts with")
}
System_Ext(trello, "Trello", "stores todo items and their status")
Component(web_server, "Web Server", "Gunicorn", "store, process, and deliver requested webpages to the user")

Rel(trello_comp, trello, "Reads & Write to", "REST API")
Rel_U(web_server, gunicorn, "Uses", "python")
Rel(flask, gunicorn, "Uses")
Rel(flask, trello_comp, "Uses")

@enduml