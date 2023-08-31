
# ![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.002.jpeg)

# <a name="_toc144312451"></a><a name="_toc144312452"></a><a name="_toc144312453"></a>"Sistema de Apoyo Ciudadano y Gubernamental basado en el estándar 311 para optimizar la comunicación y cumplir con las necesidades de la comunidad."
# <a name="_toc144312454"></a>**Por: Jesús Antonio Gutiérrez Aguilar**

##

# Tabla de contenido
`    `[Portada	1](#_toc144312451)

[Agradecimiento	2](#_toc144312455)

[Introducción	2](#_toc144312456)

[Problemas en los Servicios Municipales:	3](#_toc144312457)

[Cómo un Sistema de Comunicación Ciudadana Puede Ayudar:	3](#_toc144312458)

[Estándar Open311	4](#_toc144312459)

[El Sistema 311:	4](#_toc144312460)

[Beneficios del Estándar 311:	4](#_toc144312461)

[Comunicación Eficaz Basada en el Estándar 311:	5](#_toc144312462)

[Ubicación en git-hub	5](#_toc144312463)

[Modelos, descripción y relaciones de base de datos	5](#_toc144312464)

[Descripción de las tablas	5](#_toc144312465)

[Diagrama de modelos o base de datos	8](#_toc144312466)

[Diseño de Pantallas y Documentación en Ausencia de Prototipo: Avance hacia una Interfaz Finalizada.	9](#_toc144312467)

[Manual del sistema	10](#_toc144312468)

[Pantalla Inicial del sistema	10](#_toc144312469)

[Administrador:	11](#_toc144312470)

[Ciudadano	12](#_toc144312471)

[Funcionario	18](#_toc144312472)



##








## <a name="_toc144312455"></a>**Agradecimiento** 

**Querido maestro Zahir Ortega Gutiérrez,**

Queremos expresar nuestro más sincero agradecimiento por el excepcional apoyo y paciencia que nos brindó a lo largo de este proceso de capacitación y aprendizaje. Su dedicación como asesor, profesor y mentor ha sido fundamental para nuestro crecimiento y comprensión en el desarrollo de este proyecto.

Valoramos enormemente su compromiso y disposición para guiarnos en cada paso del camino. Su habilidad para explicar conceptos complejos de manera clara y su disposición para responder a nuestras preguntas en cualquier momento, incluso en horas inhabituales a través de WhatsApp, son ejemplos palpables de su compromiso con nuestro aprendizaje y éxito.

Además, queremos destacar su enfoque en fomentar la creatividad y la resolución de problemas, lo cual nos permitió abordar los desafíos con confianza y buscar soluciones innovadoras.

Su dedicación y experiencia han dejado una huella perdurable en nuestra formación y desarrollo. Estamos profundamente agradecidos por su apoyo inquebrantable y estamos seguros de que las habilidades y conocimientos adquiridos bajo su orientación nos serán de gran utilidad en nuestros futuros empeños.

Una vez más, le extendemos nuestro más sincero agradecimiento por todo lo que ha hecho por nosotros. Esperamos que esta relación continúe siendo una fuente de inspiración y aprendizaje en los años venideros.

Con gratitud y admiración,

Jesús Antonio Gutiérrez Aguilar
##




## <a name="_toc144312456"></a>**Introducción**
En cualquier sociedad, la relación entre la ciudadanía y el gobierno es fundamental para garantizar un funcionamiento eficiente y una mejora continua de los servicios municipales. Sin embargo, a menudo surgen desafíos en la comunicación y coordinación entre ambas partes. Problemas en los servicios municipales, como la recolección irregular de basura, fallas en el alumbrado público, fugas de agua y baches en las calles, son situaciones que impactan directamente en la calidad de vida de los ciudadanos y la imagen de la ciudad.
### <a name="_toc144312457"></a>Problemas en los Servicios Municipales: 

1\. Recolección Irregular de Basura: La falta de un horario consistente para la recolección de basura puede llevar a la acumulación de residuos en las calles, lo que contribuye a la insalubridad y la proliferación de plagas.

2\. Fallas en el Alumbrado Público: Las lámparas de alumbrado público que no funcionan adecuadamente pueden causar zonas oscuras que afectan la seguridad de los ciudadanos, aumentando el riesgo de delitos y accidentes.

3\. Fugas de Agua: Las fugas en el sistema de suministro de agua no solo desperdician un recurso escaso, sino que también pueden causar daños en infraestructuras y calles, generando problemas adicionales.

4\. Baches en las Calles: Los baches y deterioro en las calles pueden dañar vehículos y crear obstáculos para la movilidad, afectando el tráfico y causando accidentes.

### <a name="_toc144312458"></a>Cómo un Sistema de Comunicación Ciudadana Puede Ayudar:
La implementación de un sistema como el que hemos diseñado puede tener un impacto significativo en la solución de estas problemáticas y en la mejora de la relación entre la ciudadanía y el gobierno.

1\. Rápida Notificación de Problemas: Los ciudadanos pueden reportar problemas como recolección irregular de basura, fallas en el alumbrado, fugas de agua y baches directamente a través de una plataforma en línea. Esto permite que el gobierno tenga conocimiento inmediato de los problemas.

2\. Seguimiento y Priorización:  El sistema permite al gobierno llevar un registro detallado de los reportes recibidos, priorizar los problemas según su gravedad y asignar recursos de manera eficiente para su resolución.

3\. Transparencia y Participación: Al brindar a los ciudadanos la posibilidad de reportar y dar seguimiento a los problemas, se fomenta la transparencia en la gestión municipal y la participación activa de la comunidad en la mejora de su entorno.

4\. Comunicación Bidireccional: El gobierno puede responder a los reportes, proporcionando actualizaciones sobre el estado de resolución de problemas. Esta comunicación bidireccional genera confianza y mejora la percepción de la eficacia gubernamental.

5\. Datos para la Toma de Decisiones: La recopilación de datos sobre los problemas reportados y su resolución proporciona información valiosa para la toma de decisiones estratégicas en la planificación de servicios municipales.

En resumen, un sistema de comunicación ciudadana eficiente permite a los ciudadanos tener un canal directo para informar sobre problemas en los servicios municipales. Al mismo tiempo, empodera al gobierno para abordar rápidamente estas problemáticas y mejorar la calidad de vida de los ciudadanos. La interacción constante y la colaboración entre la ciudadanía y el gobierno son la base para una comunidad más segura, eficiente y agradable para vivir.
###
## <a name="_toc144312459"></a>**Estándar Open311**
En el contexto de la mejora de la comunicación entre el gobierno y la ciudadanía para resolver problemáticas en los servicios municipales, es esencial destacar la importancia de los estándares reconocidos en la industria. Uno de estos estándares es el "Estándar 311", una norma establecida para facilitar la comunicación y resolución de problemas entre los ciudadanos y las entidades gubernamentales.
### <a name="_toc144312460"></a>El Sistema 311:
El sistema de comunicación ciudadana que hemos desarrollado se apoya en el estándar 311 para brindar una experiencia eficiente y efectiva tanto para los ciudadanos como para el gobierno. El Estándar 311 establece una estructura y protocolos para la gestión de solicitudes y reportes de problemas por parte de la ciudadanía.

### <a name="_toc144312461"></a>Beneficios del Estándar 311:
1\. Uniformidad:  Al adherirse al Estándar 311, el sistema asegura una estructura uniforme en la presentación de reportes y solicitudes por parte de los ciudadanos. Esto facilita la clasificación, priorización y resolución de los problemas por parte del gobierno.

2\. Interoperabilidad: El Estándar 311 permite que los sistemas y plataformas desarrollados por diferentes entidades gubernamentales sean compatibles entre sí. Esto facilita la colaboración y el intercambio de información en beneficio de los ciudadanos.

3\. Eficiencia: Al seguir los protocolos del Estándar 311, el proceso de presentación y resolución de reportes se vuelve más ágil y eficiente. La estructura uniforme y los flujos de trabajo predefinidos agilizan la gestión de problemas.

4\. Seguimiento y Métricas: El Estándar 311 proporciona métricas y pautas para medir la eficacia del sistema y la satisfacción de los ciudadanos. Esto permite evaluar continuamente el desempeño y realizar mejoras basadas en datos concretos.

### <a name="_toc144312462"></a>Comunicación Eficaz Basada en el Estándar 311:
La adopción del Estándar 311 en el sistema de comunicación ciudadana refleja el compromiso del gobierno en brindar un servicio de calidad y en consonancia con las mejores prácticas internacionales. Esta elección permite establecer una comunicación eficaz, rápida y estructurada entre los ciudadanos y el gobierno, facilitando la resolución de problemas y la mejora constante de los servicios municipales.

En resumen, la integración del Estándar 311 en el sistema de comunicación ciudadana refuerza la eficiencia, la uniformidad y la interoperabilidad en la gestión de reportes y solicitudes de los ciudadanos. Esto no solo mejora la calidad de vida de los ciudadanos, sino que también fortalece la relación entre el gobierno y la comunidad al proporcionar un canal efectivo y estandarizado para abordar y resolver los problemas del día a día.

## <a name="_toc144312463"></a>**Ubicación en git-hub**
La ubicación del proyecto se encuentra en la siguiente dirección:

<https://github.com/Jesus-007-cmd/CiudadaniaConectada>


## <a name="_toc144312464"></a>**Modelos, descripción y relaciones de base de datos**
### <a name="_toc144312465"></a>Descripción de las tablas
#### Tabla User (Autenticación de Django):
**username**: Nombre de usuario único para cada usuario.

**password**: Contraseña del usuario (se guarda de forma segura).

**email**: Dirección de correo electrónico del usuario.

**first\_name:** Nombre del usuario.

**last\_name:** Apellido del usuario.
#### Relaciones:

**UsuarioFuncionario**: La tabla UsuarioFuncionario tiene una relación uno a uno con la tabla User, la tabla user **puede ser** 1 o 0 usuario funcionario. Esto se utiliza con el fin de poder ampliar información de los funcionarios ya que la información de ellos si es importante en el sistema para futuros cambios tener una base de datos de la productividad de cada uno o su desempeño así conocer los problemas que han resuelto.
#### Tabla Open311ReporteProblema:
**titulo**: Título del reporte de problema.

**descripcion**: Descripción detallada del problema reportado.

**categoria**: Categoría a la que pertenece el problema. Este campo puede ser editado en un futuro para dar posibles categorías y no generar demasiada información.

**estatus**: Estado actual del reporte. Este campo se pensaba escribir lo que se ha avanzado por eso quedo como texto, sin embargo, será cambiado a boleano en el que true se indica como finalizado y false como pendiente. De momento se manejará guardando el texto tal cual como finalizado o pendiente.

**direccion**: Dirección donde se encuentra el problema.

**latitud**: Coordenada de latitud (opcional).

**longitud**: Coordenada de longitud (opcional).

**fecha\_creacion**: Fecha y hora de creación del reporte.

**fecha\_ultima\_actualizacion**: Fecha y hora de la última actualización.

**id\_ciudadano**: ID del ciudadano que creó el reporte.

**imagen**: Imagen adjunta al reporte (opcional). Este permitirá subir alguna fotografía que permita mostrar evidencia del problema reportado.

**archivo\_adjunto**: Archivo adjunto al reporte (opcional). Este permitirá subir algún documento o fotografía que muestre evidencia mas contundente del problema.

Relaciones:

**AvanceReporte**: Relación de "uno a muchos" con la tabla AvanceReporte. Un reporte **tiene** 1 o varios avances a lo largo del tiempo hasta llegar a su solución final. Cada avance puede ir siendo asignado a nuevos funcionarios para en casos donde un funcionario solo este reclasificando la información o delegando las tareas. Un funcionario **Responde o da soluciones**

**UsuarioFuncionario**: Relación de "uno a uno" con la tabla UsuarioFuncionario. Indica el funcionario ha avanzado en el reporte.
#### Tabla SolicitudInformacion:
**titulo**: Título de la solicitud de información.

**descripcion**: Descripción detallada de la solicitud.

**estatus**: Estado actual de la solicitud. Si esta finalizado o sin revisión. Se creo como texto este campo, ya que no se determinaba si poner información del avance a la solicitud, en un futuro este campo se puede cambiar para falso o verdadero indicando verdadero para finalizado o falso que aún no se ha resuelto.

**fecha\_creacion**: Fecha y hora de creación de la solicitud.

**fecha\_ultima\_actualizacion**: Fecha y hora de la última actualización.

**archivo\_adjunto**: Archivo adjunto a la solicitud (opcional). Este permitirá subir algún documento o fotografía para mejor descripción de la solicitud de información.

**comentario**: Comentario relacionado con la solicitud en el que se dará respuesta a la información que solicito el usuario
#### Relaciones
**id\_ciudadano**: ID del ciudadano que **crea** la solicitud el cual tendrá una relación 1 a 1 con la tabla de user

**id\_funcionario**: ID del funcionario encargado de atender la solicitud. El cual tendrá una relación 1 a 1 con la tabla de user que esta a su vez se relaciona con la tabla usuariofuncionario y servirá para identificar el funcionario que **responde** a la solicitud de información.

#### Tabla AvanceReporte:
**solicitud**: Llave foránea a la tabla Open311ReporteProblema. Indica el reporte de problema asociado al avance.

**fecha\_avance**: Fecha y hora del avance.

**comentario**: Comentario relacionado con el avance.

**funcionario**: ID del funcionario que realizó el avance.

Relaciones:

**Open311ReporteProblema**: Relación de "muchos a uno" con la tabla Open311ReporteProblema. Cada avance está asociado a un reporte y permite dar bitácora de los avances o soluciones que se les está dando. Un usuario **Responde a solicitudes o da avance a reportes**

#### Tabla UsuarioFuncionario:
**id\_funcionario**: Llave primaria y también una llave foránea a la tabla User. Se utiliza para relacionar el perfil de funcionario con el usuario.

**cargo**: Cargo o puesto del funcionario.

**departamento**: Departamento o área en la que trabaja el funcionario.

**telefono\_contacto**: Número de teléfono de contacto del funcionario.

**horario\_trabajo**: Horario de trabajo del funcionario.

especialidad: Especialidad o experiencia del funcionario (opcional).

**foto\_perfil**: Imagen de perfil del funcionario (opcional).

Relaciones:

**User**: Relación uno a uno con la tabla User. Cada perfil de funcionario está asociado con un usuario. Un usuario **puede ser** un funcionario.

### <a name="_toc144312466"></a>Diagrama de modelos o base de datos 

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.003.png)

## <a name="_toc144312467"></a>**Diseño de Pantallas y Documentación en Ausencia de Prototipo: Avance hacia una Interfaz Finalizada.**

#### Descripción:
En el proceso de desarrollo del sistema de comunicación ciudadana y gestión de servicios municipales, se ha optado por un enfoque de diseño de pantallas y documentación en lugar de crear un prototipo inicial. Esta decisión ha sido tomada considerando diversos factores que han influido en el diseño del sistema web. Sin embargo en caso de necesitar observar su diseño puedes dirigirte directamente a la opción de manual del sistema.

Si bien los prototipos son herramientas valiosas para visualizar conceptos y funciones preliminares de un sistema, en este caso específico se ha preferido avanzar directamente hacia la creación de pantallas basadas en el diseño final. Esto se debe a una serie de razones estratégicas:

**1. Claridad en la Visión del Producto:** El diseño final del sistema ya ha sido conceptualizado y definido con precisión en colaboración con los stakeholders y equipos de desarrollo. Por lo tanto, la creación directa de las pantallas refleja con mayor exactitud la visión del producto final, evitando desviaciones potenciales que pueden surgir en la fase de prototipado.

**2. Reducción de Duplicación de Esfuerzos:** La elaboración de prototipos puede requerir recursos significativos, y en ocasiones, puede surgir la necesidad de rehacer aspectos del diseño una vez que se llega al diseño final. Al optar por el diseño de pantallas directamente, se evita la duplicación de esfuerzos y se optimiza el tiempo de desarrollo. Además que no se conto con suficiente tiempo para el desarrollo de este sistema ya que redujeron significativamente los tiempos de entrega.

**3. Foco en la Interfaz Final:** El sistema se orienta hacia la creación de una interfaz finalizada y funcional que brinde a los usuarios una experiencia realista y consistente. Al evitar el paso del prototipo intermedio, los diseñadores y desarrolladores pueden concentrarse en garantizar que la interfaz cumpla con los estándares y la calidad deseada desde el principio.

**4. Alcance y Complejidad del Sistema:** Dada la envergadura del proyecto y la diversidad de funciones que el sistema debe soportar, se ha considerado más eficiente y efectivo trabajar directamente en el diseño de las pantallas. Esto asegura que todas las características necesarias se integren adecuadamente en el producto final.

Aunque el proceso de diseño de pantallas prescinde de la etapa de prototipado tradicional, se está complementando con una documentación detallada que describe las funcionalidades, flujos de trabajo y características de la interfaz. Esta documentación proporcionará a los equipos involucrados una guía precisa para el desarrollo y permitirá una implementación coherente y efectiva del sistema.

En última instancia, la elección de avanzar directamente con el diseño de pantallas y la documentación busca agilizar el proceso de desarrollo y garantizar la entrega de un sistema que refleje fielmente las necesidades y expectativas de los usuarios, al tiempo que maximiza la eficiencia de los recursos disponibles.

## <a name="_toc144312468"></a>**Manual del sistema**
El Sistema de Comunicación Ciudadana y Gestión de Servicios Municipales es una plataforma tecnológica diseñada para mejorar la interacción y colaboración entre los ciudadanos y el gobierno local. Su objetivo principal es proporcionar un canal eficiente y transparente a través del cual los ciudadanos puedan reportar problemas, solicitar información y participar activamente en la mejora de los servicios municipales.
## <a name="_toc144312469"></a>**Pantalla Inicial del sistema**
Se ha creado una Pantalla Inicial que permite a los usuarios acceder a las funcionalidades y características del sistema en tres roles diferentes: Administrador, Ciudadano y funcionario. Esta pantalla inicial es una herramienta didáctica diseñada para ilustrar de manera clara y concisa las capacidades del sistema y cómo se adaptan a las necesidades de diferentes tipos de usuarios:

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.004.png)
###
### <a name="_toc144312470"></a>Administrador: 
Los usuarios con el rol de Administrador tienen acceso a funciones de administración como dar de alta usuarios funcionarios, así como ver los usuarios funcionarios actuales, por motivos de tiempo no se realizó funciones para desactivar usuarios o incluso eliminar usuarios sin embargo puede realizarse una mejora a este sistema futuramente si es que lo solicitan. 

Para hacerlo se creo como prueba un usuario administrador:

Username: adminjesus

Password: ghdl@G58PP

#### Iniciar sesión como administrador:
Para hacerlo se realiza nos pide las credenciales:

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.005.png)
#### Pantalla de administración:
- #### Dar de alta un usuario funcionario.
En esta parte del sistema se podrá dar de alta nuevos usuarios funcionarios, así como la visualización de los mismos, como se menciono anteriormente se pueden dar las mejoras para dar de desactivar o activar a los usuarios, otras nuevas como roles, o eliminar usuarios.

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.006.png)

Para hacerlo es necesario llenar los campos, el sistema permite elegir una imagen para poder descargar bajar en la barra de desplazamiento vertical y presionar el botón **crear usuario funcionario:**


![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.007.png)

- #### Ver usuarios funcionarios registrados
Si nos desplazamos en la misma pantalla de administración, en la parte inferior se pueden observar los usuarios funcionarios dados de alta como se muestra a continuación:

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.008.png)


### <a name="_toc144312471"></a>Ciudadano
En esta opción, los usuarios con el rol de Ciudadano pueden acceder a las funcionalidades destinadas a los ciudadanos. Esto incluye la capacidad de reportar problemas en la comunidad, hacer solicitudes de información y como mejoras del sistema se podría realizar la participación de encuestas o discusiones relacionadas con el municipio.
#### Iniciar sesión como ciudadano:
La pantalla inicial de inicio de sesión tiene la facultad de poder crear nuevos usuarios con validación de correo electrónico, también se puede recuperar la contraseña y se cuenta con función para regresar al menú anterior como se muestra a continuación:

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.009.png)

**Iniciar sesión como ciudadano**. - Si eres un usuario registrado puedes acceder al sistema escribiendo tu nombre de usuario y contraseña y finalmente presionar este botón. Para acceder a esta opción es a través del formulario de inicio del sistema como se mencionó en la sección anterior.

**Registrarse**. - En esta opción podrás dar de alta un usuario utilizando un nombre de usuario cualquiera que no exista, una contraseña o password, repetir esa contraseña o password y tu correo electrónico.

Si se requiere acceder a está pantalla es través de la pantalla inicial, elegir la opción de Acceso ciudadano y en la pantalla de inicio de sesión elegir la opción de registrarse. 

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.010.png)

Un ciudadano no requerirá información personal ya que hoy en día existen leyes que protegen a las personas como la Ley Federal de Datos personales y en las cuales no es necesario reportar algún problema o solicitar alguna información si eres un ciudadano.

Es muy importante que cuando elijas una contraseña o password no lo olvides y para evitar el error de capturarlo mal en el registro se te pide la opción de volverlo a escribir y así asegurarse de que escribiste el password o contraseña que requerías usar.

**Regresar**. – En esta última opción te permite volver al menú inicial donde solicitamos el acceso que se desee a los diferentes usuarios:

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.011.png)

#### Interfaz inicial de ciudadano
En esta interfaz un ciudadano puede crear solicitudes de información, reportar un problema al municipio, ver sus solicitudes, así como su status y ver sus reportes de problemas así como el estado actual si finalizado o no.

Para acceder a esta pantalla es a través de la ruta Acceso Ciudadano, e iniciar sesión como ciudadano:

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.012.png)
#### Generar un reporte de un problema 
Para que un ciudadano pueda generar los reportes es necesario acceder esta opción la cual es a través de través de la ruta Acceso Ciudadano, e iniciar sesión como ciudadano y finalmente la opción Generar un reporte:

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.013.png)

Una vez dentro se visualizarán opciones para capturar un reporte:

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.014.png)

Como se puede observar se agrego funcionalidad de subir una imagen en la cual se puede evidenciar el problema a reportar, incluso se pueden subir archivos por los que se pueden subir documentos con más imágenes o alguna otra información relevante, como mejor descripción del problema etc.

Existe un campo dirección en el que se pondrá la ubicación de la dirección y si queremos ser más precisos y se cuenta con un móvil en el lugar de los hechos se puede capturar la ubicación gps del problema así se podría realizar una llegada mas eficiente mediante Google maps.

Realizar una Solicitud de Información

Los ciudadanos también tienen la opción de realizar solicitudes de información sobre diversos temas, como regulaciones municipales, eventos comunitarios o programas de gobierno. Estas solicitudes se gestionan de manera eficiente y transparente a través del sistema. Para acceder esta opción la cual es a través de través de la ruta de Acceso Ciudadano, e iniciar sesión como ciudadano y finalmente la opción **Realizar una Solicitud de Información**:

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.015.png)

Una vez dentro de dicha opción nos mostrará la siguiente pantalla:

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.016.png)

Como se puede observar se cuenta con el titulo y descripción de la solicitud de información también con la opción de agregar un archivo o imagen por si es necesario.

Una vez llenos los datos solo hay que presionar el botón enviar, o si se desea cancelar dicha solicitud simplemente el botón regresar.

Ver mis solicitudes realizadas

Gestión de Avances: Una vez que se ha realizado un reporte o una solicitud, el sistema permite un seguimiento continuo del proceso. Los ciudadanos pueden recibir actualizaciones sobre el estado de sus reportes, incluidos los avances realizados por los funcionarios municipales.

Para acceder esta opción la cual es a través de la ruta de Acceso Ciudadano, e iniciar sesión como ciudadano y finalmente la opción **Ver mis solicitudes realizadas**:

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.017.png)

Dentro de esta opción se puede ver si se ha tenido algún avance o no:

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.018.png)

Como se puede observar si no ha sido respondida nos mostrara que aún no ha tomado ningún funcionario y la respuesta estará vacía. En el código solo se programó ver el identificador del funcionario, pero si se solicita se agregara el nombre o lo que se requiera.

Ver mis reportes realizados

Para ver si mis reportes de problemas ya han sido respondidos debo entrar en esta opción. Para acceder esta opción la cual es a través de la ruta de Acceso Ciudadano, e iniciar sesión como ciudadano y finalmente la opción **Ver mis reportes realizados**:

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.019.png)

Una vez dentro se pueden observar todo el seguimiento que han dado los funcionarios a mis peticiones como se muestra a continuación:

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.020.png)

En esta opción ya se cuenta con un avance sin embargo se cuentan con errores como corregir y escribir el nombre del funcionario en el avance realizado
### <a name="_toc144312472"></a>Funcionario
Los usuarios con el rol de funcionario pueden acceder a la sección reservada para el personal del gobierno municipal. Aquí, los funcionarios pueden ver los reportes y solicitudes asignadas, registrar avances, comunicarse con los ciudadanos y gestionar la resolución de problemas.
#### Iniciar sesión como funcionario:
La pantalla inicial de inicio de sesión solo es posible elegir usuario y contraseña, ya que la creación de usuarios funcionarios es a través del administrador del sistema, a modo que se solicite un cambio futuramente. El diseño de esta interfaz es muy sencillo y se muestra a continuación

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.021.png)
#### Interfaz inicial de funcionario
En esta interfaz un funcionario ver los reportes de la ciudadanía y ahí mismo contestarlos y resolverlos, también puede ver la lista de solicitudes de información, así como la contestación de las mismas y por último ver reportes por fecha. Esta interfaz quedo demasiado limitada por él hecho de que se recorto los tiempos de entrega del sistema. Para acceder a esta pantalla es a través de la ruta de Acceso funcionario, e iniciar sesión como funcionario: 

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.022.png)

Ver reportes de la ciudadanía

En esta interfaz, los funcionarios tienen la capacidad de visualizar los reportes de problemas presentados por la ciudadanía. La pantalla muestra una lista de los reportes disponibles, cada uno con su título, descripción, estado actual, dirección, entre otros datos como se muestra en la siguiente imagen. Esta interfaz brinda una vista general de los problemas, lo que permite a los funcionarios priorizar y abordar los casos de manera efectiva. Para acceder a esta pantalla es a través de la ruta de Acceso funcionario, e iniciar sesión como funcionario: y entrar en la opción **ver reportes de la ciudadanía:**

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.023.png)

En esta ventana a su vez se pueden ver los reportes finalizados si uno se dirige más abajo:

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.024.png)

Dar respuesta a un problema reportado por el usuario

Para poder atender los reportes de los ciudadanos es a través de la ruta de Acceso funcionario, e iniciar sesión como funcionario: y entrar en la opción ver reportes de la ciudadanía y elegir la opción **dar respuesta** en el problema reportado elegido**:**

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.025.png)

Aquí el funcionario se podrá concentrar más claro en el problema y podrá dar una respuesta en el campo Responder de la parte inferior. En caso de que solo quiera comentar un avance o que esta en proceso el funcionario no debe activar la opción de finalizado. En caso de que quiera ver los avances de ese problema en la parte inferior se muestran los avances:

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.026.png)

Listas de solicitudes de información

En esta interfaz, los funcionarios pueden acceder a una lista de todas las solicitudes de información presentadas por la ciudadanía. Cada solicitud se muestra con su título, estado actual y fecha de creación. Al seleccionar una solicitud específica, los funcionarios pueden ver más detalles, como la descripción de la solicitud, cualquier archivo adjunto y los comentarios proporcionados por la ciudadanía. Esta interfaz ayuda a los funcionarios a gestionar y responder a las solicitudes de información de manera oportuna, lo que mejora la transparencia y la comunicación con la ciudadanía. Para acceder a esta pantalla es a través de la ruta de Acceso funcionario, e iniciar sesión como funcionario y entrar en la opción **Listas de solicitudes de información:**

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.027.png)

Al igual que los reportes también viendo cada una de las solicitudes se puede dar respuesta de manera individual. Al final se mostrarán todas las solicitudes que ya han sido respondidas.

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.028.png)

Dar respuesta a una solicitud de información

Para poder responder las solicitudes de información de los ciudadanos es a través de la ruta de Acceso funcionario, e iniciar sesión como funcionario: y entrar en la opción de listas de solicitudes de información y elegir la opción **dar respuesta** en la solicitud de preferencia del funcionario o que considere de mayor relevancia ya sea por tiempo u otros factores**:**

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.029.png)

En esta ventana se podrá responder en el campo inferior a la solicitud y finalmente guardar respuesta. En caso de información no hay avance acerca de ella por que al dar respuesta se da la información solicitada.

Reportes por fecha

En esta interfaz, los funcionarios pueden filtrar y visualizar los reportes de problemas y solicitudes de información en función de un rango de fechas específico. Pueden seleccionar una fecha de inicio y una fecha de finalización para delimitar el período de tiempo deseado. Después de aplicar los filtros, la pantalla mostrará una lista de reportes que se crearon dentro del rango de fechas seleccionado. Esta funcionalidad permite a los funcionarios analizar los datos de manera más específica y obtener información sobre los problemas y solicitudes que surgieron en un período determinado. Para acceder es a través de la ruta de Acceso funcionario, e iniciar sesión como funcionario y entrar en la opción **Reportes por Fecha.**

Por falta de tiempo no fue posible agregar funciones adicionales sin embargo se pretende que con estas interfaces administrar de manera eficiente los problemas y solicitudes presentados por la ciudadanía, facilitando una respuesta y solución más rápida y efectiva.

![](Aspose.Words.fb195606-d9a7-49a0-8c88-19f1c2d7ab3c.030.png)


Beneficios del Sistema 

- Documentación y Transparencia: Todos los reportes, solicitudes y avances se documentan de manera exhaustiva en el sistema. Esto promueve la transparencia en la gestión de servicios municipales y facilita la rendición de cuentas tanto para el gobierno como para los ciudadanos.
- Mejora la eficiencia en la comunicación y resolución de problemas.
- Facilita la participación activa de los ciudadanos en la mejora de su entorno.
- Permite una gestión más efectiva de los recursos municipales.
- Fomenta la transparencia y la rendición de cuentas en la administración pública.
- Crea un canal de colaboración entre ciudadanos y funcionarios municipales.
- Proporciona una plataforma tecnológica moderna que se adapta a las necesidades actuales.
- En resumen, el Sistema de Comunicación Ciudadana y Gestión de Servicios Municipales es una solución integral que busca fortalecer la conexión entre el gobierno y los ciudadanos, promoviendo una gestión más ágil y transparente de los servicios municipales.




2

