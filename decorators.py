from typing import Any, Callable


# region Decorators
def experimental(func: Callable) -> Callable:
    # Decorator for classes or functions that are used for experimental purposes only.
    print(f"Experimental function/class {func.__name__} used.")
    return func


def url(_url: str) -> Callable:
    # Used for documenting a function with external URL.
    def _decorator(function):
        def wrapper(*args, **kwargs):
            print(f"Doc: {_url}")
            result = function(*args, **kwargs)
            return result
        return wrapper
    return _decorator


@url("https://www.codementor.io/sheena/advanced-use-python-decorators-class-function-du107nxsv")
@url("https://stackoverflow.com/questions/1938048/high-precision-clock-in-python")
def timed(func: Callable) -> Callable:
    def new_function(*args, **kwargs):
        import time
        sec = time.time_ns()
        x = func(*args, **kwargs)
        sec = (time.time_ns() - sec) / (10 ** 9)
        print(f"Elapsed Time = {sec}")
        return x
    return new_function
# endregion


# region Design Patterns
def pattern(cls: Any) -> Any:
    return cls


@pattern
def gof_pattern(cls: Any) -> Any:
    # Patterns described in Design Patterns: Elements of Reusable Object-Oriented Software book by
    # Erich Gamma, John Vlissides, Ralph Johnson, and Richard Helm (aka Gang of Four pattern or GoF)
    return cls


@pattern
def creational(cls: Any) -> Any:
    # A creational pattern abstracts the instantiation process of simple and composite objects.
    # Creational patterns deal with delegation. They are focused on creating new objects and groups of related objects.
    # These patterns will create objects for you, meaning that you don't have to create them directly.
    return cls


@pattern
def structural(cls: Any) -> Any:
    # A structural pattern groups objects into larger structures. Handle the way objects are composed into new objects.
    # The focus of structural patterns is aggregation. They define ways to compose objects in a way that creates new
    # functionality from the constituent parts. They help us create software components.
    return cls


@pattern
def behavioural(cls: Any) -> Any:
    # A behavioral pattern defines communication between objects and with distribution of responsibilities.
    # Behavioral patterns are big on consultation they talk about responsibilities between objects. Unlike structural
    # patterns, which only specify a structure, behavioral patterns define communication paths and messages
    return cls


@pattern
def concurrency(cls: Any) -> Any:
    # Patterns needed in the world of parallel programming.
    # Concurrency patterns deal with cooperation. They make a system composed of multiple components, running in
    # parallel, work together. The main concerns of concurrency patterns are resource protection and messaging.
    # Pattern-Oriented Software Architecture: Patterns for Concurrent and Networked Objects, Volume 2, by
    # Douglas C Schmidt, Michael Stal, Hans Rohnert, and Frank Buschmann
    return cls


@pattern
def data_pattern(cls: Any) -> Any:
    # Patterns that relate to how data is processed and transfered
    return cls


@pattern
def micro_service(cls: Any) -> Any:
    # Microservice Architecture pattern or Microservices. The idea is that we can build an application as a set of
    # loosely coupled, collaborating services. In this architectural style.
    # Services can be developed and deployed independently of one another.
    # Described in Mastering Python Design Patterns - Second Edition book by Kamon Ayeva, Sakis Kasampalis
    return cls


# region Creational Patterns
@creational
@gof_pattern
def factory(cls: Any) -> Any:
    # Defines an interface for creating a single object. Subclasses can then decide which class to instantiate.
    return cls


@creational
@gof_pattern
def abstract_factory(cls: Any) -> Any:
    # Create entire families of related objects but without the need to specify their classes.
    return cls


@creational
@gof_pattern
def builder(cls: Any) -> Any:
    # Abstracts the construction of a complex object, and allows the same process to create different representations.
    return cls


@creational
@gof_pattern
def prototype(cls: Any) -> Any:
    # Specifies how to create objects based on a template object that is cloned to produce new objects.
    return cls


@creational
@gof_pattern
def singleton(cls: Any) -> Any:
    # Ensures that a class has only one instance. It also provides a common point of access to that instance.
    return cls


@creational
def multiton(cls: Any) -> Any:
    # Similar to singleton. It allows multiple named instances, while serving as the only way of accessing them.
    return cls


@creational
def dependency_injection(cls: Any) -> Any:
    # Used to send specific instances of depended objects into a class (injecting them), instead of the class creating
    # them directly.
    return cls


@creational
def lazy_initialization(cls: Any) -> Any:
    # Delays the creation of an object or the calculation of a value until it is actually needed. In the GoF book, it
    # appeared as a virtual proxy.
    return cls


virtual_proxy = lazy_initialization


@creational
def object_pool(cls: Any) -> Any:
    # Recycles objects to avoid the expensive acquisition and creation of resources. A special case, connection pool,
    # is well-known to all database programmers.
    return cls


@creational
def prototype(cls: Any) -> Any:
    # Specifies how to create objects based on a template object that is cloned to produce new objects.
    return cls


@creational
def resource_aquisition_is_initialization(cls: Any) -> Any:
    # RAII- Pattern ensures that resources are properly released by tying them to the lifespan of an object.
    return cls


raii = resource_aquisition_is_initialization
# endregion


# region Structural Patterns
@structural
@gof_pattern
def adapter(cls: Any) -> Any:
    # Converts the interface of a class into another interface expected by a client.
    return cls


wrapper = adapter


translator = adapter


@structural
@gof_pattern
def bridge(cls: Any) -> Any:
    # Decouples an abstraction from its implementation, which allows the two to vary independently.
    return cls


@structural
@gof_pattern
def composite(cls: Any) -> Any:
    #  This composes from the hierarchies of more basic objects.
    return cls


@structural
@gof_pattern
def decorator(cls: Any) -> Any:
    # Allows an object to take additional responsibilities, in addition to its original interface. Decorators are an
    # alternative to subclassing for an extending functionality.
    return cls


@structural
@gof_pattern
def facade(cls: Any) -> Any:
    # Combines a set of interfaces exposed by subsystems into a simpler interface that is easier to use.
    return cls


@structural
@gof_pattern
def flyweight(cls: Any) -> Any:
    # Uses data-sharing to efficiently support large numbers of similar objects.
    return cls


@structural
@gof_pattern
def proxy(cls: Any) -> Any:
    # Provides a replacement for another object so it can control access to.
    return cls


@structural
def extension_object(cls: Any) -> Any:
    # Allows adding of a functionality to a hierarchy without changing that hierarchy.
    return cls


@structural
def front_controller(cls: Any) -> Any:
    # Used when designing web applications and provides a centralized entry point for request handling.
    return cls


@structural
def marker(cls: Any) -> Any:
    # This allows us to associate metadata with a class.
    return cls


@structural
def module(cls: Any) -> Any:
    # Groups several related elements into one conceptual entity.
    return cls


@structural
def twin(cls: Any) -> Any:
    # Helps simulating multiple inheritance in programming languages that don't support this feature.
    return cls
# endregion


# region Behavioral Patterns
@behavioural
@gof_pattern
def chain_of_responsibility(cls: Any) -> Any:
    # Object-oriented version of an if ladder idiom (if  ... elif ... elif ... else ...)
    # It works by constructing a chain of processing objects.
    return cls


@behavioural
@gof_pattern
def command(cls: Any) -> Any:
    # Encapsulates a request as an object. It is especially useful for building user interfaces where it allows for the
    # support of undoable operations.
    return cls


@behavioural
@gof_pattern
def interpreter(cls: Any) -> Any:
    # Defines a representation of a language grammar and gives an interpreter for that grammar.
    return cls


@behavioural
@gof_pattern
def iterator(cls: Any) -> Any:
    # Provides a way to access elements of an aggregate object (list, array, symbol table, tree, and so on)
    # sequentially, without exposing the underlying implementation of that object.
    return cls


@behavioural
@gof_pattern
def mediator(cls: Any) -> Any:
    # Defines an object that handles interaction between other objects. This pattern supports loose coupling by
    # preventing objects from referring to one another explicitly.
    return cls


@behavioural
@gof_pattern
def memento(cls: Any) -> Any:
    # Specifies how to store and restore an object's internal state without violating encapsulation.
    return cls


@behavioural
@gof_pattern
def observer(cls: Any) -> Any:
    # It provides another way to prevent tight coupling in a system, by setting up a system where a change of objects
    # results in all of its dependents being notified about the change.
    return cls


publish_subscribe = observer


@behavioural
@gof_pattern
def state(cls: Any) -> Any:
    # Allows an object to change its behavior when there is a change to its internal state.
    return cls


@behavioural
@gof_pattern
def strategy(cls: Any) -> Any:
    # A family of algorithms that can be used interchangeably.
    return cls


@behavioural
@gof_pattern
def template(cls: Any) -> Any:
    # Defines a skeleton of on operation and defers some steps to subclasses.
    return cls


@behavioural
@gof_pattern
def visitor(cls: Any) -> Any:
    # Specifies an operation that is performed on all elements of an object's internal structure
    return cls


@behavioural
def blackboard(cls: Any) -> Any:
    # Artificial intelligence (AI) pattern for combining different data sources.
    return cls


@behavioural
def null_object(cls: Any) -> Any:
    # Removes the reason for using a nil, null, None pointer, by providing a special, default value for a class.
    return cls


@behavioural
def servant(cls: Any) -> Any:
    # Defines an object that implements a common functionality for a group of classes.
    return cls


@behavioural
def specification(cls: Any) -> Any:
    # Provides support for business logic that can be recombined by chaining the rules together with boolean operations.
    return cls


@behavioural
def state_design(cls: Any) -> Any:
    # An object can encapsulate multiple behaviors based on its internal state.
    # Defined in Learning Python Design Patterns - Second Edition by Chetan Giridhar
    return cls


objects_for_states = state_design
# endregion


# region Concurrency Patterns
@concurrency
def active_object(cls: Any) -> Any:
    # Hides the concurrency by implementing asynchronous method inside an object, which serves as a scheduler for
    # handling requests.
    return cls


@concurrency
def binding_properties(cls: Any) -> Any:
    # Combines multiple observers to force synchronization on properties in different objects.
    return cls


@concurrency
def blockchain(cls: Any) -> Any:
    # A decentralized way for storing data in a linked list protected with cryptographic means.
    return cls


@concurrency
def compute_kernel(cls: Any) -> Any:
    # Executes the same calculation many times in parallel, differing only on integer input parameters. It is frequently
    # related to GPU calculation.
    return cls


@concurrency
def double_checked_locking(cls: Any) -> Any:
    # Reduces the overhead of acquiring a lock in a safe manner.
    return cls


@concurrency
def event_based_asynchronous(cls: Any) -> Any:
    # Defines a way of executing parallel operations where a caller is notified when a worker finishes the execution.
    return cls


@concurrency
def future(cls: Any) -> Any:
    # Pushes a calculation into a background and replaces it with a promise that a result will be available in the
    # future.
    return cls


@concurrency
def guarded_suspension(cls: Any) -> Any:
    # Manages operations that depend on a two-part condition: a precondition that must be satisfied and a lock that must
    # be acquired.
    return cls


@concurrency
def join(cls: Any) -> Any:
    # Provides a way to write distributed and parallel systems, by message passing.
    return cls


@concurrency
def lock(cls: Any) -> Any:
    # Protects shared resources by implementing a locking mechanism.
    return cls


@concurrency
def lock_striping(cls: Any) -> Any:
    # Optimizes locking, by replacing a single global lock with a set of specialized locks.
    return cls


@concurrency
def messaging_design(cls: Any) -> Any:
    # Based on the interchange of information between components in the system.
    return cls


mdp = messaging_design


@concurrency
def monitor(cls: Any) -> Any:
    # Combines locking with a mechanism for signalling other threads that their condition was met.
    return cls


@concurrency
def optimistic_initialization(cls: Any) -> Any:
    # Reduces the cost of locking by replacing it with the small probability of extraneous objects being created and
    # thrown away.
    return cls


@concurrency
def pipeline(cls: Any) -> Any:
    # Specifies a way of decoupling thread dependencies by passing small subsets of data from one worker thread to
    # another through a message-passing pipeline.
    return cls


@concurrency
def reactor(cls: Any) -> Any:
    # Reactor object that provides an asynchronous interface to resources that must be handled synchronously.
    return cls


@concurrency
def read_write_lock(cls: Any) -> Any:
    # Allows multiple objects to simultaneously read a shared resource, but forces exclusive access for write
    # operations.
    return cls


@concurrency
def scheduler(cls: Any) -> Any:
    # Controls when threads may execute single-threaded code.
    return cls


@concurrency
def thread_pool(cls: Any) -> Any:
    # A parallel version of an object pool creational pattern that provides a pool of worker threads that execute
    # numerous tasks.
    return cls


@concurrency
def thread_specific_storage(cls: Any) -> Any:
    # Allows us to use global memory that is local to a thread.
    # In Delphi for example, we implement this by declaring a variable with the threadvar directive.
    return cls
# endregion


# region Data Patterns
@data_pattern
def data_transfer_object(cls: Any) -> Any:
    # Pattern used when simple objects usually stored within struct or union or record are passed between various parts
    # of the program. Typically those objects do have methods and just data field members such as fields and properties.
    return cls


dto = data_transfer_object


@data_pattern
def data_access_layer(cls: Any) -> Any:
    # Classes that wrap the access to do databases.
    return cls
# endregion


# region MVC/MVVM Patterns
@pattern
def mvc_pattern(cls: Any) -> Any:
    return cls


@pattern
def mvvm_pattern(cls: Any) -> Any:
    return cls


@mvc_pattern
@mvvm_pattern
def model(cls: Any) -> Any:
    # Internal representation of the data.
    return cls


@mvc_pattern
@mvvm_pattern
def view(cls: Any) -> Any:
    # View is the screen presentation of GUI, web page
    return cls


@mvc_pattern
def controller(cls: Any) -> Any:
    # Coordinates changes between the Model and View.
    return cls


@mvvm_pattern
def model_view(cls: Any) -> Any:
    return cls


# region View Patterns
@view
@url("URL : http://www.delphifeeds.com/go/f/123041")
def alert_view(cls: Any) -> Any:
    # Read only notification to the user. Such as MessageDlg or ShowMessage.
    return cls


@view
def selection_view(cls: Any) -> Any:
    # Form to find some kind of reference key for locating data for the user, often through a database lookup
    # operation.
    return cls


@view
def data_entry_view(cls: Any) -> Any:
    # CRUD form for data amendments.
    return cls


@view
def domain_management_view(cls: Any) -> Any:
    # Usually this is your main form.
    return cls
# endregion
# endregion


# region Micro-services Patterns
@micro_service
def retry(cls: Any) -> Any:
    # Implement retry logic for web service calls, so that we pass through the issue, by calling the service again,
    # maybe immediately or after some wait time (such as a few seconds).
    return cls


@micro_service
def circuit_breaker(cls: Any) -> Any:
    # Wrap a fragile function call (or an integration point with an external service) in a special (circuit breaker)
    # object, which monitors for failures. Once the failures reach a certain threshold, the circuit breaker trips, and
    # all further calls to the circuit breaker return with an error, without the protected call being made at all.
    return cls


@micro_service
@url("https://docs.microsoft.com/en-us/previous-versions/msp-n-p/dn589799(v=pandp.10)")
def cache_aside(cls: Any) -> Any:
    # In situations where data is more frequently read than updated, applications use a cache to optimize repeated
    # access to information stored in a database or data store. In some systems, that type of caching mechanism is
    # built-in and works automatically. When this is not the case, we have to implement it in the application ourselves,
    # using a caching strategy that is suitable for the particular use case.
    return cls


@micro_service
@url("https://docs.microsoft.com/en-/azure/architecture/patterns/throttling")
def throttling(cls: Any) -> Any:
    # Based on limiting the number of requests a user can send to a given web service in a given amount of time, in
    # order to protect the resources of the service from being overused by some users.
    return cls


@pattern
@url("https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm")
def rest(cls: Any) -> Any:
    # Representational State Transfer (REST) is a Web service design pattern. It is different from SOAP based web
    # services. REST services do not require XML, SOAP or WSDL service-API definitions. The concept originally comes
    # from a PhD's dissertation
    return cls
# endregion


# region Other Patterns
@pattern
def type_safe_enum(cls: Any) -> Any:
    # Define a class representing a single element of the enumerated type and provide no public constructor.
    return cls


smart_enum = type_safe_enum


@pattern
def smart_pointer(cls: Any) -> Any:
    return cls


@pattern
def business_delegate(cls: Any) -> Any:
    # An intermediate class decouples between presentation-tier clients and business services.
    return cls


@pattern
def intercepting_filter(cls: Any) -> Any:
    # A pluggable component design to intercept incomming requests and outgoing responses, provide common services in a
    # standard manner (independently) without changing core processing code.
    return cls


@pattern
def service_locator(cls: Any) -> Any:
    # Centralizing distributed service object lookups, providing a centralized point of control, acting as a cache that
    # eliminates redundant lookups.
    return cls
# endregion
# endregion
