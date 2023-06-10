@startuml Context Diagram
!include <C4/C4_Container>

LAYOUT_TOP_DOWN()
title Context Diagram for To-Do App

Person(app_user ,"Application User")
System(todo_app, "To-Do Application", "Allows users to see, create and modify todo items and their 'Done' status")
Rel(app_user, todo_app, "Uses", "HTTPS")

@enduml