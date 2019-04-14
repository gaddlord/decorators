# decorators
Python modules with various decorators such as design pattern decorators, documentation decorators, etc.

Using this module one would be able to better document the source code by adding descriptive decorators on classes in cases where design
patterns are used.

In the example below we:
* oranment the class with @singleton to know that we would have only one tray icon in the application
* we mark it as @experimental which would remind that this is not finished implementation by writing in the output window a warning message that experimental code is used
* we let other developers know the implementation was taken from Stack Overflow article
* we display in the output window the amount of milliseconds passed while the show method was executed
~~~~
from models.code.decorators import singleton, experimental, url, timed

@singleton
@experimental
@url("https://stackoverflow/some_fancy_tray_icon_hint_i_used")
class Tray:
    """Display a tray icon in the tray bar using the standard application icon and name as tooltip."""
    @timed
    def show():
      pass
~~~~

List of Decorators:
* experimental
* url
* timed

Design Patterns:
* Creational
  * factory
  * abstract_factory
  * builder
  * prototype
  * singleton
  * multiton
  * dependency_injection
  * lazy_initialization
  * object_pool
  * prototype
  * resource_aquisition_is_initialization
* Structural
  * adapter
  * bridge
  * composite
  * decorator
  * facade
  * flyweight
  * proxy
  * extension_object
  * front_controller
  * marker
  * module
  * twin
* Behavioural
  * chain_of_responsibility
  * command
  * interpreter
  * iterator
  * mediator
  * memento
  * observer
  * state
  * strategy
  * template
  * visitor
  * blackboard
  * null_object
  * servant
  * specification
  * state_design
* Concurency
  * active_object
  * binding_properties
  * blockchain
  * compute_kernel
  * double_checked_locking
  * event_based_asynchronous
  * future
  * guarded_suspension
  * join
  * lock
  * lock_striping
  * messaging_design
  * monitor
  * optimistic_initialization
  * pipeline
  * reactor
  * read_write_lock
  * scheduler
  * thread_pool
  * thread_specific_storage
* Data
  * data_transfer_object
  * data_access_layer
* MVC/MVVM
  * model
  * view
    * alert_view
    * selection_view
    * data_entry_view
    * domain_management_view
  * controller
  * model_view
* Micro-service
  * retry
  * circuit_breaker
  * cache_aside
  * throttling
  * rest
* Other
  * type_safe_enum
  * smart_poiner
  * business_delegate
  * intercepting_filter
  * service_locator
