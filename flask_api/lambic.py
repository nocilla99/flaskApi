from clases import Estilo, Subestilo

lambic_desc ="""Cervezas compuesta por cebada malteada y un 30-40% de trigo sin maltear creadas a partir de fermentación espontánea. Este es un proceso característico únicamente del distrito de Payottenland, cerca de Lembeek (Bélgica), en el valle del Zenne, siendo por lo general aceptada sólo esta denominación de origen para recibir el apelativo Lambic, Lambiek o Lámbica. 

En este tipo de cerveza, la temperatura de fermentación no es tan importante como el ambiente en que sucede, pues se dejan fermentar durante más de 3 meses en barricas de roble abiertas, normalmente situadas en el ático del edificio. Sus fabricantes afirman que obtienen los mejores resultados en las frías noches de otoño. Estos fabricantes coinciden en que el entorno debe permanecer inalterado, hasta el punto de mantener hasta las telarañas de la bodega intactas, preservando el pequeño ecosistema todo lo posible. Éste es el único tipo de cerveza que siempre tiene su fermentación primaria en barril y, además, la de mayor duración.

En estas barricas se produce la mezcla con la levadura salvaje en suspensión en el aire pues, solo en esta región se han identificado más de 160 microorganismos no controlados. Esta familia de cervezas es la única en usar levaduras salvajes de forma intencional, convirtiéndolas en Ale ya que, a día de hoy, no se conoce la existencia de ningún tipo de levadura salvaje tipo Lager en Europa. Estas levaduras salvajes, lejos de la optimización de las industriales, dejan muchos azúcares y compuestos volátiles de sabor (ésteres) en la cerveza, dando como resultado un producto con toques a vino, frutas y fenoles de gran complejidad. El lúpulo que se le añade, cuya cantidad es unas 6 veces superior al de la mayoría de las cervezas, es intencionalmente viejo para aportar el menor amargor y aroma posible, siendo sus propiedades antibióticas las que realmente interesan. Para saborizar, se usan frutas que le dan un aroma característico. Cabe mencionar también que su fase de hervido del mosto es particularmente larga, llegando a las 5 horas, lo cual eleva su concentración de azúcar al reducirse el volumen del mosto.

La maduración dura un mínimo de 6 meses sin haber un máximo de tiempo, aunque la más consumidas rondan entre 6 meses y 3 años. Si madura menos de 1 verano, se conoce como lámbica joven (Jonge) o Vos (“zorro” en holandés) y ofrece un sabor simple pero fuertemente ácido con notas lácticas, manteniendo más azúcares fermentables y un aspecto turbio. Si su maduración llega a 2 o 3 veranos, se considera lámbica vieja (Oude). Esta cerveza aporta ese característico sabor “salvaje” del Zenne, más complejo y con un color más claro y rosado. El resultado es una cerveza agria, seca y con un contenido alcohólico inferior a 6% ABV. Dependiendo del tipo, pueden ser más dulces o tener más gas.

Su historia se remonta al menos al siglo XV, convirtiéndose en la especialidad local de Bruselas desde mediados del XVIII. Hay varias teorías sobre el origen de su nombre: Una afirma que es una corrupción de Lembeek, una ciudad de la zona, mientras que otra especula que deriva de “alambique”, nombre con el que los conquistadores españoles denominaron a las instalaciones en que se elaboraban. Su elaboración no fue del todo definida y regulada por Bélgica y la UE hasta finales del siglo XX, habiéndose exportado desde entonces por otros países con cada vez mayor popularidad. Si bien únicamente las cervezas elaboradas en el valle del Zenne son verdaderas lámbicas, algunos fabricantes extranjeros han probado a elaborar las suyas propias usando levaduras salvajes cultivadas a partir de lámbicas sin filtrar.
"""


lambic_pura = Subestilo('Lambic Pura',
    """Siendo el subestilo más representativo de la familia Lambic y el más difícil de encontrar, madura durante al menos 3 años y, si se sigue la tradición, nunca es embotellado para no perder sus principales características, por lo que es ideal servirlo directamente desde el barril. Se conoce también como lámbica pura. Se recomienda su consumición en vaso Flauta, Tulipa, Pinta o incluso vaso Taster a unos 5-10ºC.
    Es importante remarcar que su nombre varía según el fruto utilizado: Cerezas agrias (Kriek), frambuesas (Frambozen), uvas moscatel (Druiven) y fresas (Aardbeien) entre otros."""
    ,'El color oscila entre dorado y ámbar, por lo general turbio. El envejecimiento las vuelve algo más oscuras y limpias. Poco que comentar de su espuma, pues es casi inexistente al tener una muy baja retención.'
    ,'Este subestilo presenta un cuerpo bajo y una carbonatación sin patrón reconocible, ya que puede ir de baja a alta.'
    ,'Debido a su tradición frutal, es previsible que el aroma muestre a menudo intensos ésteres afrutados, ignorando el lúpulo, el cual puede a veces manifestarse en leves matices herbáceos y florales. El final es seco.'
    ,'Una de las características principales de este estilo es su sabor principalmente ácido, parecido al de un vino blanco o sidra, gracias a la levadura. El papel del lúpulo o de la malta es bastante secundario.'
    ,'Por último, el contenido alcohólico suele oscilar entre 5 y 8% ABV, por lo general en torno a 6% ABV.',None)

lambic_fruit = Subestilo('Lamic Fruit','Este subestilo nace de la adición de frutos rojos en pleno proceso de fermentación para que maduren con el mosto durante al menos 6 semanas. Es entonces cuando se produce una fermentación secundaria por el azúcar que estos frutos contienen, añadiéndole un aroma y sabor característicamente frutal. En ocasiones, se usa como base una Oude a la que se añade una Jonge justo antes del embotellado. La maduración en el caso de la Kriek tradicional se prolonga desde verano hasta primavera. Se recomienda tomarla en vaso Tulipa, vaso Pinta o vaso Snifter a una temperatura ideal entre 5 y 10ºC.'
    ,'Sin duda, una de las principales propiedades de este subestilo es su color rosado o rojizo, dependiendo de la fruta utilizada, a menudo con cierta turbidez.'
    ,'Llama la atención también su cuerpo medio-alto, destacable para una Lambic, y su carbonatación alta.'
    ,'Inevitablemente, su aroma es afrutado por los adjuntos, con escasa presencia de lúpulo o malta.'
    ,'Aunque la intensidad del sabor depende de la receta de cada cerveza, su sabor es suave y característicamente afrutado. También tiene el típico toque ácido de las Lambic, siendo a menudo distinguible en su acidez el uso de levadura Brett.'
    ,'Esta cerveza cuenta con un contenido alcohólico muy variable, ya que suele oscilar entre 5.5 y 9% ABV.',None)



lambic_geuze =Subestilo('Lambic Geuze',
    'Mezcla de cervezas lámbicas Jonge y Oude que se embotellan y envejecen durante 2 o 3 años, entrando en juego los azúcares aún sin fermentar en la Jonge. Se cree que su nombre deriva del término “géiser” por su alta carbonatación, aunque otros lo relacionan con los Geus, disidentes liberales locales en contra de la presencia española en tiempos de los Austrias. Se recomienda su consumición en vaso Tulipa o vaso Pinta a una temperatura cercana a los 5ºC.'
    ,'A menudo con cierta turbidez debido a la segunda fermentación en botella, su color oscila entre dorado y ámbar. Una propiedad a tener en cuenta en este subestilo es la espuma, pues es más densa y consistente que en otras Lambics.'
    ,'Estas cervezas muestran un cuerpo muy bajo y una carbonatación alta.'
    ,'Sin diferenciarse mucho de las cervezas de su familia, su aroma exhibe fuertes ésteres afrutados y matices de índole agria y ácida. La malta y el lúpulo, al ser viejo, se notan poco o nada.'
    ,'Con un final seco, su sabor es delicadamente ácido, sin el menor resquicio de lúpulo y con ciertos ésteres afrutados también en el paladar.'
    ,'En el apartado alcohólico, se puede definir como una Lambic más fuerte (7- 9% ABV)',None)

lambic_faro =Subestilo('Lambic Faro',
    """Este subestilo se elabora a menudo mezclando lámbicas Jonge y Oude (aunque a veces solo con Jonge) con la característica de añadir azúcar de caramelo o jarabe de azúcar para rebajar el cuerpo y edulcorar el sabor. El resultado es una cerveza ligera y dulce que era antaño ofrecida a toda la familia, incluso a niños. Cuando se embotella, la segunda fermentación no se deja acabar, ya que se pasteuriza quedando siempre algo de azúcar en el producto final y así manteniendo el mayor dulzor posible. Algunas, sin embargo, no se embotellan sino que se sirven en la propia cafetería belga, ofreciendo a veces al cliente un recipiente y revolvedor para añadir el azúcar allí mismo. Se desconoce el origen del nombre aunque se ha propuesto una relación con la palabra en latín para harina (“farina”), asociada a la creencia de que se trataba de un vino de grano. Se recomienda su consumición en vaso Tulipa o vaso Pinta a una temperatura ideal de unos 5ºC. 
    Aunque algo difíciles de encontrar y al borde la extinción, existe un grupo de cervezas llamado Mars que no son más que una versión diluida y, por lo tanto, más débil de una Faro (en torno a 2% ABV), elaborada tradicionalmente en marzo para aplacar el calor. Para conseguir el producto final, se mezcla una Faro con una cerveza Meers, nombre dado a una cerveza ligera elaborada con el mosto residual de una Lámbica pura. Dado que el principal uso histórico conocido de la Meers es realizar este blending con la Faro, ha pasado a considerarse una variante de esta, rara vez consumiéndose de otra manera."""
    ,'Como la mayoría de los subestilos de Lambic, el color oscila entre dorado y ámbar aunque estas cuentan con una espuma blanca regular y de larga retención.'
    ,'Se considera una cerveza fácil de beber con un cuerpo bajo y una carbonatación alta.'
    ,'Aroma'
    ,'Tal y como se ha apuntado anteriormente, su sabor es muy dulce aunque cuenta con una acidez moderada, a menudo con toque especiado.'
    , 'Estas cervezas nunca han contado con una gran carga alcohólica. Sin ir más lejos, a día de hoy, su contenido alcohólico ronda entre 2% y 5% ABV.',
    None)

subestilos_lambic = [lambic_pura,lambic_fruit,lambic_geuze,lambic_faro]


LAMBIC = Estilo("Lambic",lambic_desc,subestilos_lambic)