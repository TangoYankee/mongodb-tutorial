# lending-library
Demonstrate a [RESTFul](https://restfulapi.net/) API created with Flask and MongoDB to manage materials for a library.

## restfulapi.net
REST is an acronym for **RE**presentational **S**tate **T**ranser.

### Six Guiding Principles/Constraints of REST
1. **Client-Server**  
The concerns of the user interface are separated from concerns of data storage
2. **Stateless**  
Each request contains enough information to fulfill the request.
It does not rely on exernal context/session data.
3. **Cacheable**
Responses to requests distinguish between being cacheable or not-cachable.
A cacheable response gives the client the right to reuse data for equivalent requests
in later instances
4. **Uniform Interface**  
Adhering to constraints in four domains, the interface is generalized to countless applications
   - Identification of resources
   - Manipulation of resources through representations
   - self-descriptive messages
   - hypermedia as the engine of application state
5. **Layered System**  
Architecture is composed of hierarachies which limit each component from seeing
beyond its immediate layer of interaction.
6. **Code on Demand** (Optional)  
Code may be downloaded and executed as applets or scripts

### HTTP Request Methods
REST is a desining principle separate from HTTP. However, it is commonly implemented in web design
and utilizes HTTP requests to execute its principles.
- GET
- PUT
- POST
- DELETE
- HEAD
- CONNECT
- OPTIONS
- TRACE
- PATCH
