from clases import Estilo, Subestilo
lager_desc = """
Estas cervezas son también llamadas de baja fermentación (bottom / low fermentation) debido a que la levadura Lager es más frágil que la levadura Ale, asentándose en la parte de abajo de la mezcla, actuando a temperaturas más bajas (5-9ºC) y durante más tiempo. Aunque depende del estilo, una Ale suele estar lista en menos de 1 mes, mientras que una Lager puede tardar entre 1 y 3 meses, aunque algunos ejemplos con alto contenido alcohólico superan los 6 meses. En la última parte del proceso, estas cervezas son almacenadas en bodegas (Lagern significa “almacenar” en alemán) a baja temperatura (0-2ºC) con el objetivo de limpiar las partículas residuales y estabilizar los sabores. Su baja fermentación es el motivo por el cual se suele usar agua blanda, o sea, pobre en sales minerales. Se suele recomendar beberlas a temperaturas bajas (3-7ºC).
Son conocidas generalmente por tener un bajo contenido alcohólico, una alta carbonatación, escaso o nulo poso, poca turbidez y un cuerpo muy ligero, aunque en el mundo de la cerveza siempre hay excepciones. La levadura Lager, que fermenta a menor temperatura y consume mucha más cantidad de azúcar que la levadura Ale, da como resultado cervezas más secas, limpias, atenuadas y de sabores menos complejos. Las menores temperaturas evita que se liberen tantos ésteres como en las Ales, reduciendo así los aromas afrutados frecuentes en éstas. Esto implica que la malta y el lúpulo deben brillar más por sí mismos, aún si en general son de presencia menos intensa, lo cual suele compensarse empleando más cantidad.
Históricamente, las Lagers que conocemos nacieron en Bavaria (Alemania) en el siglo XV en respuesta a la imposibilidad de elaborar cerveza en verano, pues las levaduras salvajes estivales se mezclaban con las propias de la cerveza y la contaminaban. Lo tardío de la aparición de este tipo de fermentación parece deberse a que la levadura Lager (Saccharomyces Pastorianus, también llamada S. Carlsbergensis) no es sino un híbrido entre la ya presente levadura Ale (S. Cerevisiae) y una levadura de la Patagonia (S. Eubayanus), más acostumbrada al frío, que empezó a llegar a Europa de manera accidental como consecuencia del nuevo tráfico transatlántico. Mientras que en otros lugares se creaban amplias remesas en primavera (sobre todo marzo) para consumir en los meses cálidos, los bávaros llevaban a cabo el almacenamiento (lagerung en alemán) de la cerveza en interiores fríos, como cuevas alpinas. Fue entonces cuando comprobaron que no solo se conservaba mejor, pues la aún desconocida levadura descendía al fondo por el frío evitando posibles contaminaciones en la superficie, sino que maduraba hasta dar un producto más limpio y equilibrado. La técnica de almacenamiento bávara empezó a extenderse y desarrollarse durante el siglo XIX gracias a los modernos sistemas de refrigeración. La figura clave en este proceso fue el cervecero muniqués Gabriel Sedlmayr, que donó esta innovadora levadura a su colega Emil Hansen de Carlsberg (Dinamarca), quien a su vez finalmente aisló el cultivo en 1883, llegando poco después también a conocidos en Heineken (Holanda). Esto inició no solo el nacimiento de las Lagers actuales sino una verdadera revolución en el mundo de la cerveza, pues su método y levadura producían un producto más estable que cualquier otro en el mercado. Hoy día, la mayoría de las cervezas producidas masivamente por las macro-cervecerías son Lagers."""


munich_helles = Subestilo('Pale Lager: Munich Helles',
                       'Uno de los estilos más populares y extendidos. Servido en vaso Pilsner, Jarra, vaso Pinta o vaso Flauta a unos 4ºC. Comparado con una Pilsner, tiene más cuerpo y mayor contenido maltoso pero su sabor es menos lupulado.'
                        ,'Como su nombre indica, son cervezas rubias, claras y de espuma poco densa, irregular y efímera. ',
'En este subestilo, tanto el cuerpo como la carbonatación son medios, superior el primero al de muchas otras Lagers.',
'El aroma es claramente maltoso, a menudo complementado con cierta presencia de levadura, con baja o nula presencia de lúpulo pues se usan ejemplares nobles.',
'Su sabor muestra un gran carácter maltoso dulce con recuerdos florales y poco amargor lupulado. A pesar de tener un cuerpo más completo que muchas Lagers, es reconocida por ser muy refrescante y tener un final ligeramente seco.',
'No son cervezas muy potentes pues su contenido alcohólico oscila entre 4 y 6% ABV.',None)
pale_lager_dortmunder = Subestilo(
    titulo='Pale Lager: Dortmunder / European Export',
    descripcion='Aunque a veces el apelativo Export se usa en otras regiones para referirse a cervezas que cumplen la ley de pureza alemana, el estilo es propio de Dortmund, de ahí su nombre. Si se tuviera que describir esta cerveza con sólo un adjetivo, este sería equilibrado pues no destaca ni su contenido lupulado ni su malta. Servido en vaso Flute o vaso Pilsner a 7-10ºC. Se considera el paso intermedio entre el amargor de una Pils y el dulzor de una Helles pues tiene más cuerpo y un final menos seco que una Pils pero es más amarga y menos dulce que una Helles.',
    aspecto='La imagen de este subestilo es muy llamativa al ser de un color dorado profundo con una corona espumosa densa.',
    cuerpo='Tanto el cuerpo como la carbonatación son de nivel medio.',
    aroma='Su aroma conjuga malta y lúpulo, este último noble y de matices florales, sin gran intensidad.',
    sabor='Su característica más importante en el sabor es el perfecto balance entre el dulce de la malta y el amargor floral del lúpulo noble, ambos bastante bajos. Se suelen encontrar matices especiados y florales de lúpulo y algo de tueste en la malta.',
    alcohol='Mostrándose ligeramente superior a las Lagers habituales, este subestilo presenta un contenido alcohólico situado entre 5 y 6% ABV.',
    subestilos=None
)

pale_lager_california_common = Subestilo(
    titulo='Pale Lager: California Common / Steam Beer / Dampfbier',
    descripcion='Subestilo estadounidense que destaca por utilizar un método de fermentación único en recipientes muy anchos y de escasa profundidad (parecido a una paellera gigante), lo que permite que su levadura Lager especial fermente como es costumbre en la parte baja, pero a una temperatura superior a lo normal, más propia de una Ale. El producto final ofrece elementos tanto de Ale como de Lager. La denominación Steam Beer es actualmente propiedad intelectual de la San Francisco’s Anchor Brewing Company. Debido a esto, el resto de empresas debe usar su otro nombre, California Common. Servido en vaso Pinta a 10-13ºC. Difiere de otras Pale Lagers o de algunas Amber Ales en el tipo de lúpulo, concediéndole un intenso aroma y sabor más a madera y a menta que cítrico. El estilo era común en California hacia el siglo XIX cuando, a falta de hielo u otros medios para enfriar el recipiente, se buscaron otras maneras de hacer cervezas de baja fermentación y dieron con amplios recipientes que aprovechaban las frescas temperaturas de la bahía.',
    aspecto='El rango de color que muestra esta cerveza se sitúa entre ámbar y cobre claro. Además, su corona espumosa es blanca radiante con una gran retención.',
    cuerpo='Su apelativo Steam Beer (Cerveza de vapor) es debido a su alto contenido carbónico, el cual supuestamente hacía que el recipiente silbase por el vapor. Esta intensa carbonatación procede en buena parte de una segunda fermentación en el recipiente. Por otro lado, muestra un cuerpo medio, con un tacto algo seco al final.',
    aroma='Con matices acaramelados y tostados gracias a la malta, presenta un aroma que logra un equilibrio en nariz con el leve perfil lupulado que recuerda a madera y menta.',
    sabor='Su sabor dulce a malta es tostado y caramelizado pero moderado, siendo el amargor del lúpulo el que pesa más en la balanza en la mayoría de los casos, aunque tampoco demasiado alto. Exhibe a menudo también matices afrutados.',
    alcohol='Sin destacar en el apartado de Lagers, el contenido alcohólico oscila entre 4.5 y 6% ABV.',
    subestilos=None
)

pale_lager_japanese_rice_lager = Subestilo(
    titulo='Pale Lager: Japanese Rice Lager',
    descripcion='Cerveza ligera tanto en aroma como en sabor, graduación y lupulación. Como su nombre indica, estas cervezas se elaboran con arroz y cebada. Servido en vaso Pilsner o Jarra a 4-6ºC. Este estilo, junto a la cerveza japonesa como tal, nació en el siglo XIX como imitación de los métodos alemanes. Si bien en principio se trataba de un producto reducido para clases medias y altas, marginal con respecto al sake, esto dio un vuelco tras la Segunda Guerra Mundial convirtiéndose las marcas Asahi, Sapporo y Kirin en titanes que arrinconaron al sake e incluso se extendieron en mercados extranjeros hasta la actualidad. El estilo como tal nació en tiempos de posguerra, lo cual explica su ligereza y sobriedad.',
    aspecto='No destaca por su color entre los diferentes estilos de Lager, pues es rubia y limpia.',
    cuerpo='Cuenta con un cuerpo ligero y un contenido carbónico alto, haciendo de esta cerveza una cerveza muy refrescante.',
    aroma='En el apartado del aroma, hay que destacar su leve aroma a lúpulo.',
    sabor='Suelen tener un sabor maltoso con un amargor moderado y un final seco característico.',
    alcohol='Su contenido alcohólico suele rondar los 4.5% ABV.',
    subestilos=None
)

pale_lager_dry_beer = Subestilo(
    titulo='Pale Lager: Dry Beer',
    descripcion='Apelativo de origen japonés usado para denominar una adaptación menos intensa de la Diat Pils alemana. Servido en vaso Flauta o Pinta a 4-7ºC. Tras su debut en el país nipón con la Asahi Super Dry en 1987, la Dry Beer se empezó a distribuir en diferentes mercados extranjeros, muy especial en EEUU donde se redujo aún más la intensidad, exhibiendo una graduación alcohólica y contenido calórico convencionales, pero apenas sabor o final en boca.',
    aspecto="No destaca por su color entre los diferentes estilos de Lager, pues es rubia y limpia.",
    cuerpo='Como la Japanese Rice Lager, es de cuerpo muy ligera.',
    aroma='Como la Japanese Rice Lager, es ligera en aroma.',
    sabor='Como la Japanese Rice Lager, es ligera tanto en sabor como en lupulación, con menos azúcar y aún menos postgusto. Su ausencia de dulzor es lo que le vale el apelativo de “cerveza seca”.',
    alcohol='Su contenido alcohólico es promedio, hacia 5% ABV, lo que no deja de ser superior al 4.5% ABV habitual en el país.',
    subestilos=None
)

subs_pale_lager = [munich_helles,pale_lager_dortmunder,pale_lager_california_common
,pale_lager_japanese_rice_lager,pale_lager_dry_beer]

pale_lager = Subestilo(
    titulo='Pale Lager',
    descripcion='Uno de los estilos más populares y extendidos. Servido en vaso Pilsner, Jarra, vaso Pinta o vaso Flauta a unos 4ºC. No debe confundirse con una Pilsner, la cual tiene más aroma, más amargor y generalmente más cuerpo. Se puede acercar más a una Munich Helles, pero algo más débil en general. El estilo nace en Europa el siglo XIX, cuando se adaptan los métodos habituales para elaborar Pale Ales a las levaduras de baja fermentación y el lagerung alemán. Nació imitando a la por entonces popular Munich Helles.',
    aspecto='Como su nombre indica, son cervezas rubias, claras y de espuma poco densa, irregular y efímera.',
    cuerpo='Otras de sus dos características más importantes son su cuerpo ligero y su contenido carbónico, estando entre medio y alto.',
    aroma='El aroma no es muy destacable ya que es casi inexistente. En algunos ejemplos, se puede detectar algo de aroma a malta y casi nada a lúpulo, a veces con presencia de ésteres frutales.',
    sabor='Aunque su sabor es también suave debido al poco uso de malta y el uso de lúpulos poco aromáticos o amargos, este puede recordar un poco al pan según la presencia de levadura.',
    alcohol='El contenido alcohólico no es muy alto, normalmente situado entre 3 y 6% ABV.',
    subestilos=subs_pale_lager
)

#--------------------

pilsen_pilsner_pils = Subestilo(
    titulo='Pilsen / Pilsner / Pils',
    descripcion='Estilo clásico de la República Checa y muy popularizado en su variante alemana. A pesar de su perfil simple a primera vista, su elaboración es delicada y requiere gran precisión y esfuerzo. Servido en vaso Pilsner o Flauta a 4-6ºC. La primera en su estilo, la Plzeňský Prazdroj o Pilsner Urquell (“Original de Pilsen”), fue creada en 1842 en esta ciudad checa de Bohemia combinando la levadura y maduración Lager bávara, recientemente popularizadas por Gabriel Sedlmayr, con malta pálida al estilo inglés. El apelativo Urquell se añadió en 1898, cuando ya habían surgido muchas otras incluso en Alemania, para dejar claro que fue la primera. El resultado, que buscaba competir con las nuevas y exitosas Lagers de Bavaria, fue la primera cerveza dorada y clara en una época donde todas las demás eran oscuras y/o turbias. Éste fue el comienzo de una exitosa tendencia hasta este aspecto, en especial cuando empezaron a producirse masivamente recipientes transparentes de vidrio que permitían ver la cerveza al beber.',
    aspecto='Muestra un color entre dorado y ámbar, sin turbidez, y una espuma cremosa y blanca de buena retención.',
    cuerpo='Esta cerveza presenta un cuerpo entre ligero y medio y una carbonatación entre media y alta, garantizando un trago refrescante.',
    aroma='El aroma es equilibrado entre malta y un característico perfil lupulado derivado de lúpulos nobles, a menudo añadidos tardíamente (late-hopping).',
    sabor='Su sabor es predominantemente a malta pero con un claro papel del lúpulo. Destaca por un final largo, seco y lupulado.',
    alcohol='La graduación de esta cerveza oscila entre 4% y 6% ABV.',
    subestilos= None
)

#-----------------

amber_lager_rauch_stein = Subestilo(
    titulo='Amber Lager: Rauchbier/Steinbier',
    descripcion='Estilo alemán oriundo del siglo XIV y caracterizado por usar malta de cereal ahumada (“rauch” significa “humo” en alemán), secándose sobre una hoguera de madera de haya. Conocida también como cerveza ahumada de Bamberg por su ciudad de origen. Es particularmente bueno para maridar, sobre todo con platos ahumados. Servido en Jarra o vaso Pinta a 7-12ºC. Cabe mencionar la inusual Steinbier, también oriunda de Bamberg. Esta cerveza es tostada y caramelizada, preparada añadiendo al mosto rocas envueltas en caramelo ahumado calentadas a unos 1300ºC en una hoguera de madera de haya. De esta forma, los azúcares de la malta se funden con las piedras formando una oscura capa de caramelo. Una vez secas, las piedras van al tanque de maduración, donde los azúcares fermentan y aportan su característico sabor a toffee y melaza al producto final. Esta particular variante se remonta a tiempos en que las grandes calderas no eran de metal sino de madera, por lo que en lugar de fuego, se añadían las piedras candentes para llevar al mosto a temperaturas de hervido necesarias. En la actualidad, las piedras se añaden cuando el mosto ya está casi a la temperatura ideal, solo por la saborización y para dar un último empujón térmico. Debido a su rico perfil maltoso, esta cerveza se ha comparado a menudo con la Märzen.',
    aspecto='Esta cerveza presenta una amplia variedad de tonalidades, pues el color oscila entre ámbar y marrón oscuro. Presenta una espuma abundante, duradera y cremosa de color entre crema y canela.',
    cuerpo='Aunque el cuerpo puede parecer algo alto para una Lager, en general sigue siendo medio-bajo con carbonatación de media a media alta.',
    aroma='Aunque el aroma y sabor quedan inundados por el ahumado de la malta, aún es posible detectar otros matices como el caramelo. El lúpulo, a menudo noble, apenas hace acto de presencia.',
    sabor='Aunque el aroma y sabor quedan inundados por el ahumado de la malta, aún es posible detectar otros matices como el caramelo. El lúpulo, a menudo noble, apenas hace acto de presencia. El ahumado también garantiza un final seco al trago.',
    alcohol='Su contenido alcohólico oscila entre 5% y 6% ABV.',  
    subestilos=None
)


amber_lager = Subestilo(
    titulo='Amber Lager',
    descripcion='Estilo amplio, referido por lo general a la tradición americana (American Amber Lager) y caracterizado por su color ambarino y perfil maltoso. Servido en vaso Pilsner o Jarra a 7-10ºC. A pesar de las diferencias nacidas a posteriori, el origen histórico de todas estas variantes de Amber Lager viene a ser el mismo. La palabra Märzen se refería no tanto a un estilo como a un método, concretamente a la fabricación de cervezas en marzo antes de que el calor y la ausencia de refrigeración industrial estropease el proceso, para luego beberse en los meses calurosos. Esto explica su generosa graduación, la cual contribuía a su conservación. La magnitud de la producción de marzo era tal que aún quedaban muchas existencias en la entrada del otoño, coincidiendo con la Oktoberfest en septiembre, donde se convertía en la cerveza más típica. Dicho esto, si bien dicha confluencia de cerveza y festival popularizó la Märzen, lo cierto es que en Viena, hacia 1732, encontramos la primera mención al estilo, e incluso, hacia el siglo XVI, menciones a cervezas Merzen, también elaboradas en marzo por el mismo motivo. La Märzen ofrece un perfil maltoso superior, con menor presencia de lúpulo o de amargor, amén de un cuerpo y graduación (entre 5% y 6% ABV) algo más alto. Su aroma y sabor tienen un matiz cereal que recuerda al pan tostado. La llamada Oktoberfest bier se parece a la Märzen pero es casi siempre más ligera en malta, cuerpo y color, llegando a menudo al dorado, y algo más intensa en lúpulo y graduación alcohólica, encajando con el concepto alemán de Festbier (“cerveza de celebración”). La Oktoberfest ha sido comparada, en su encarnación contemporánea, con la Dortmunder Export. Esto se debe a que, recientemente, el clásico estilo festivo ha reducido a veces su perfil maltoso para equipararse al papel del lúpulo, logrando el característico equilibrio de la Dortmunder. La American Märzen/Oktoberfest se distingue solo por un papel algo más protagonista del lúpulo. Aunque históricamente es casi indistinguible de la Märzen, hoy día se habla de Vienna Style cuando el color es algo más ligero, tirando a marrón rojizo, presentando también una graduación alcohólica algo inferior y algo más de amargor que equilibra un moderado perfil maltoso. Por último, cabe mencionar que al hablar de una Amber Lager, no se puede olvidar la checa Polotmavý (“medio oscura”), más negra y conocida también como “pan bebido” por su marcado sabor a pan aunque a veces puede presentar un sabor más caramelizado debido a la variedad de maltas. Esta se diferencian de la Märzen o la Vienna Style por una mayor cantidad de lúpulo, a menudo el Saaz propio de la Pilsner. Dicho eso, hay quien considera que elaborar la cerveza en marzo y tener un carácter maltoso ya amerita el apelativo Märzen, por lo que nada impediría hablar de una Märzen Vienna Style u otras combinaciones.',
    aspecto='Como previamente se ha comentado, el color oscila entre dorado y marrón cobrizo, con un característico tono rojizo que le da su nombre. Espuma abundante y de buena retención.',
    cuerpo='Este subestilo muestra un cuerpo medio, de textura suave, y una carbonatación media.',
    aroma='Su aroma es leve a malta, con matiz tostado y/o caramelizado y posible presencia del lúpulo.',
    sabor='Lo más complejo de esta cerveza es su sabor ya que es levemente dulce y con un toque más tostado que caramelizado proveniente de la malta. Aparte, muestra un amargor moderado, complementando el dulzor con un final seco. Al igual que en el aroma, el lúpulo puede o no estar presente, oscilando entre bajo y medio-alto.',
    alcohol='Al igual que otras Lagers, el contenido alcohólico oscila entre 4% y 6% ABV.', 
    subestilos= [amber_lager_rauch_stein]
)
#------------

dark_lager = Subestilo(
    titulo='Dark Lager',
    descripcion='Estilo característicamente oscuro y suave. La Dunkel de Múnich es tan famosa que el término Münchener o Münchner se usa a menudo internacionalmente para designar cualquier Lager de color marrón oscuro. Servido en vaso Pinta a 7-10ºC. La diferencia entre ambas es que la Dunkel/Dunkles alemana, típica de Múnich, mantiene esa hegemonía de la malta mientras que la menos popular Tmavý checa se permite tener cierto carácter lupulado. No confundir con Dunkelweizen, una Ale de trigo oscura, que se diferencia entre otras características, por su cuerpo mucho más completo. La Schwarzbier (“cerveza negra” en alemán) se gana ser distinguida de la Dunkel que la inspiró por una moderada presencia del lúpulo (aunque no tanto como en la Tmavý), un cuerpo más ligero, un final más seco, y sobre todo, un color más oscuro, amén de una espuma inesperadamente amarillenta y de buena retención. La más reciente American Dark Lager, inspirada claramente en las variantes anteriores, se distingue por una mayor carbonatación y un cuerpo más ligero y limpio. Las primeras Lagers, creadas como tales hacia el siglo XVIII, fueron de color oscuro, siendo frecuente que las cerveceras alemanas tengan desde entonces una Dunkel como especialidad de la casa. El término Schwarzbier precede la generalización de las Lagers y fue en origen una cerveza oscura de alta fermentación originada en Bad Köstriz (Alemania).',
    aspecto='Este estilo muestra una gama de color entre cobre y marrón oscuro. Cuenta con una espuma blanca, ligera y duradera.',
    cuerpo='A nivel general, esta cerveza presenta un cuerpo medio-bajo y una carbonatación media.',
    aroma='En el aroma, apenas se aprecia el lúpulo, por lo general noble, atrayendo toda la atención el olor maltoso a pan, chocolate, caramelo y frutos secos.',
    sabor='Su sabor goza de cierta complejidad pues, si bien leve, logra un buen equilibrio entre el moderado y algo especiado dulzor de la malta y el más bajo amargor del lúpulo noble. El resultado es un trago refrescante y con final seco con matices de café, regaliz y cacao, pero no fuertemente tostado como las Ales oscuras.',
    alcohol='El contenido alcohólico oscila entre 4.5% y 6% ABV.',
    subestilos=None
)

#------------

bock_hellerbock = Subestilo(
    titulo='Bock: Hellerbock',
    descripcion='Podría considerarse una versión pálida de la Bock tradicional o una variante más fuerte y maltosa del estilo Munich Helles. Se suele servir en primavera, desde finales de marzo hasta mayo. Según diferentes marcas cerveceras, este estilo permite ser consumido en diferentes vasos como Goblet, Tulipa, Pilsner, Pinta, Snifter y Jarra a 7-12ºC. Aunque se suelen considerar un mismo estilo, a veces las Maibock se distinguen por ser cervezas de celebración (festbier) con más lúpulo y un color algo más oscuro dentro de los límites del estilo. La principal diferencia con la Bock tradicional es su color más pálido, su sequedad y una mayor presencia del lúpulo.',
    aspecto='La coloración de esta cerveza oscila entre rubia clara (“heller”) y ámbar claro con abundante espuma cremosa y de buena retención.',
    cuerpo='El cuerpo medio-alto, denso para una Lager, le ha merecido el apelativo de “pan líquido” en la región de Bavaria. Presenta una alta carbonatación.',
    aroma='Posee aroma y sabor maltoso que recuerdan al pan, a veces algo caramelizado, quedando el lúpulo, por lo general noble, en segundo plano aunque algo más resaltado que en otras Bocks.',
    sabor='Posee aroma y sabor maltoso que recuerdan al pan, a veces algo caramelizado, quedando el lúpulo, por lo general noble, en segundo plano aunque algo más resaltado que en otras Bocks.',
    alcohol='Su contenido alcohólico suele estar entre 6% y 8% ABV.',
    subestilos=None
)
bock_eisbock =  Subestilo(titulo='Bock: Eisbock', 
            descripcion='Subestilo de Bock con una graduación alcohólica muy alta elaborado mediante el proceso de congelación de una Dopplebock. Dado que el agua se congela antes que el etanol, eliminar el hielo (“eis”) aumenta la concentración alcohólica. El nombre hace referencia a este proceso llamado destilación por congelación y no necesariamente a una superioridad alcohólica, existiendo de hecho Dopplebocks más fuertes que muchas Eisbock. Servido en vaso Snifter a 12-15ºC. Como curiosidad histórica, esta cerveza se creó en 1890 en la cervecería Reichelbräu en la ciudad alemana de Kulmbach, cercana a República Checa. Todo sucedió de manera accidental, pues olvidaron algunos barriles de Bock al aire libre en una noche muy fría de invierno.', 
            aspecto='El color oscila entre marrón oscuro y negro, a veces con tonos rojizos.Su corona espumosa es delgada y blanca aunque bastante irregular y de baja retención.', 
            cuerpo='Presenta un cuerpo muy completo, incluso viscoso a veces y un contenido carbónico muy bajo.',
            aroma='Su aroma a alcohol es potente, destacando el carácter maltoso y achocolatado por encima de todo, con cierta presencia de ésteres afrutados. El lúpulo no llama la atención en ningún momento pues el amplio contenido maltoso no lo permite.', 
            sabor='Parecido al aroma que desprende, el sabor puede ser dulce, afrutado y especiado, pero queda a menudo eclipsado por su fuerte presencia alcohólica, siendo también casi nula la presencia del lúpulo.', 
            alcohol='Su contenido alcohólico oscila entre 8.5% y 15% ABV.', 
            subestilos=None)


subs_bock=[bock_hellerbock,bock_eisbock]

bock_bok = Subestilo(
    titulo='Bock / Bok',
    descripcion='Si bien este término (“cabra” en alemán) puede ser usado de manera genérica para denominar una cerveza fuerte, por lo general se refiere a este estilo de Lager oscura y maltosa. Conlleva un proceso de maduración algo más largo que las demás Lagers para suavizar su contenido alcohólico, inusualmente alto entre ellas. Suelen servirse en otoño, finales de invierno o primavera según el país. No confundir con la jarra Bock, propia de Alemania y caracterizada por su asa. Servido en vaso Tulipa o Jarra a 7-10ºC. La variante más cercana es la Doppelbock, típica del sur de Alemania, caracterizada por una mayor densidad de cuerpo y elevado contenido alcohólico (7.5-12% ABV), rasgos que le valen el apelativo “doble” (“doppel” en alemán) y una mayor complejidad de aroma y sabor, ahora con cierto toque licoroso. Se consideran una especialidad del sur de Alemania, siendo elaborada originalmente por monjes de Múnich y sirviéndose aún sobre todo en marzo y abril. Como curiosidad, estas cervezas exhiben a menudo el sufijo -ator en honor a la primera Doppelbock, la Paulaner Salvator. Cabe destacar la Rauchbock, que aplica el método de ahumado propio de la Rauchbier, acercando ambos estilos. La Bock original nació en el siglo XIV como una Ale más, transformándose en Lager cuando las levaduras de baja fermentación empezaron a proliferar por Alemania.',
    aspecto='Si bien se puede encontrar algún ejemplo de color dorado, el color característico suele ser entre cobre claro y marrón oscuro, sin turbidez y con espuma blanca, densa, cremosa y de buena retención.',
    cuerpo='El cuerpo se sitúa entre medio y alto y la carbonatación entre media y baja.',
    aroma='Su aroma es maltoso con matices de nueces tostadas y baja o nula presencia de lúpulo.',
    sabor='Aunque eminentemente dulce, esta cerveza puede llevar cierta cantidad de lúpulo pero nunca le roba el protagonismo a la malta. Las más claras suelen ser menos maltosas y con cierto papel de lúpulo, ofreciendo cierta sequedad.',
    alcohol='Posee graduación de al menos 6% ABV, por lo general hasta 7.5 % ABV.',
    subestilos=subs_bock
)

subestilos_lager = [pale_lager,pilsen_pilsner_pils,amber_lager,dark_lager,bock_bok]

LAGER = Estilo("Lager",lager_desc,subestilos_lager)