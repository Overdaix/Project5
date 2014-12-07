from scrapy.item import Item, Field
class Memory(Item):
    '''
    Class for the item retrieved by scrapy.
    '''
    # Here are the fields that will be crawled and stored
    Category = Field()
    Name = Field() # Game title
    Brand = Field()
    Url = Field()  # Link to product page.
    Price = Field() #Product price.
    Date = Field()  # Release date
    Name = Field() # Name of the product.
    Sku = Field()# Stock keeping unit.
    Ean = Field()# European article number.
    Description= Field() #General info about product.
    Model = Field()   #Model information.
    Type = Field() #Intern/Extern.
    Location = Field() #Inter/Extern.
    Software = Field() #Info about software provided.
    Bay = Field() #Information about compatible bay (example: 1x intern - 2.5")
    ServiceInfo = Field() #Information about service and support.
    Warranty = Field () #Information about waranty period.
    #Harddisk specific info
    Memory = Field() #Amount of memory
    Quantity = Field() #Quantity of sticks
    Size = Field()
    PriceGB = Field() #Price per gb
    Type = Field() #Type of memory
    Specification = Field() #Specs
    LowVoltage = Field()
    CASLatency = Field()
    Voltage = Field()

class Motherboard(Item):
    Category = Field()
    Name = Field() # Game title
    Brand = Field()
    Url = Field()  # Link to product page.
    Price = Field() #Product price.
    Date = Field()  # Release date
    Name = Field() # Name of the product.
    Sku = Field()# Stock keeping unit.
    Ean = Field()# European article number.
    Description= Field() #General info about product.
    Model = Field()   #Model information.
    Type = Field() #Intern/Extern.
    Location = Field() #Inter/Extern.
    Software = Field() #Info about software provided.
    Bay = Field() #Information about compatible bay (example: 1x intern - 2.5")
    ServiceInfo = Field() #Information about service and support.
    Warranty = Field () #Information about waranty period.
    #Info specific for motherboards
    Socket = Field()
    SocketAmount = Field()
    Speed = Field()
    FormFactor = Field()
    Chipset = Field()
    Type = Field()
    MaxMemory = Field()
    HarddiskBus = Field()
    CardInter = Field()
    PCIAmountx16 = Field()
    Interface = Field()
    Connection = Field()
    Chip = Field()
    Bluetooth = Field()
    USBCon = Field()
    Video = Field()
    AudioChannels = Field()
    AudioOutput = Field()
    AudioChip = Field()

class Processor(Item):
    Category = Field()
    Name = Field() # Game title
    Brand = Field()
    Url = Field()  # Link to product page.
    Price = Field() #Product price.
    Date = Field()  # Release date
    Name = Field() # Name of the product.
    Sku = Field()# Stock keeping unit.
    Ean = Field()# European article number.
    Description= Field() #General info about product.
    Model = Field()   #Model information.
    Type = Field() #Intern/Extern.
    Location = Field() #Inter/Extern.
    Software = Field() #Info about software provided.
    Bay = Field() #Information about compatible bay (example: 1x intern - 2.5")
    ServiceInfo = Field() #Information about service and support.
    Warranty = Field () #Information about waranty period.
    #Info specific for processors
    Socket = Field()
    CoreAmount = Field()
    Speed = Field()
    MaxFreq = Field()
    Specs = Field()
    BusSpeed = Field()
    Power = Field()
    Virtualisation = Field()
    VirtualType = Field()

class Power(Item):
    Category = Field()
    Name = Field() # Game title
    Brand = Field()
    Url = Field()  # Link to product page.
    Price = Field() #Product price.
    Date = Field()  # Release date
    Name = Field() # Name of the product.
    Sku = Field()# Stock keeping unit.
    Ean = Field()# European article number.
    Description= Field() #General info about product.
    Model = Field()   #Model information.
    Type = Field() #Intern/Extern.
    Location = Field() #Inter/Extern.
    Software = Field() #Info about software provided.
    Bay = Field() #Information about compatible bay (example: 1x intern - 2.5")
    ServiceInfo = Field() #Information about service and support.
    Warranty = Field () #Information about waranty period.
    #spec for power
    Power = Field()
    Capacity = Field()
    SataAmount = Field()
    MolexAmount = Field()
    PCIAmount = Field()
    CoolerAmount = Field()
    CoolerSize = Field()
    CoolerType = Field()
    CoolerLocation = Field()
    Width = Field()
    Height = Field()
    Depth = Field()

class Cooler(Item):
    Category = Field()
    Name = Field() # Game title
    Brand = Field()
    Url = Field()  # Link to product page.
    Price = Field() #Product price.
    Date = Field()  # Release date
    Name = Field() # Name of the product.
    Sku = Field()# Stock keeping unit.
    Ean = Field()# European article number.
    Description= Field() #General info about product.
    Model = Field()   #Model information.
    Type = Field() #Intern/Extern.
    Location = Field() #Inter/Extern.
    Software = Field() #Info about software provided.
    Bay = Field() #Information about compatible bay (example: 1x intern - 2.5")
    ServiceInfo = Field() #Information about service and support.
    Warranty = Field () #Information about waranty period
    #Spec for coolers
    Socket = Field()
    Attachment = Field()
    Heatpipes = Field()
    Volume = Field()
    RotationSpeedMin = Field()
    RotationSpeedMax = Field()
    Height = Field()
    Material = Field()

class GraphicsCard(Item):
    Category = Field()
    Name = Field() # Game title
    Brand = Field()
    Url = Field()  # Link to product page.
    Price = Field() #Product price.
    Date = Field()  # Release date
    Name = Field() # Name of the product.
    Sku = Field()# Stock keeping unit.
    Ean = Field()# European article number.
    Description= Field() #General info about product.
    Model = Field()   #Model information.
    Type = Field() #Intern/Extern.
    Location = Field() #Inter/Extern.
    Software = Field() #Info about software provided.
    Bay = Field() #Information about compatible bay (example: 1x intern - 2.5")
    ServiceInfo = Field() #Information about service and support.
    Warranty = Field () #Information about waranty period
    #Spec for graphicscards
    Chip = Field()
    Generation = Field()
    MinSpeed = Field()
    MaxSpeed = Field()
    Cores = Field()
    Memory = Field()
    MemoryType = Field()
    MemorySpeed = Field()
    MemoryBus = Field()
    CardInterface = Field()
    Video = Field()
    DirectX = Field()
    OpenGL = Field()
    Shader = Field()
    Resolution = Field()
    Height = Field()
    Width = Field()
    Slots = Field()
    PinAmount = Field()
    Power = Field()
    CoolerType = Field()
    Interface = Field()

class Case(Item):
    Category = Field()
    Name = Field() # Game title
    Brand = Field()
    Url = Field()  # Link to product page.
    Price = Field() #Product price.
    Date = Field()  # Release date
    Name = Field() # Name of the product.
    Sku = Field()# Stock keeping unit.
    Ean = Field()# European article number.
    Description= Field() #General info about product.
    Model = Field()   #Model information.
    Type = Field() #Intern/Extern.
    Location = Field() #Inter/Extern.
    Software = Field() #Info about software provided.
    Bay = Field() #Information about compatible bay (example: 1x intern - 2.5")
    ServiceInfo = Field() #Information about service and support.
    Warranty = Field () #Information about waranty period
    #
    Type = Field()
    FormFactor = Field()
    Panel = Field()
    Materials = Field()
    GraphMaxLength = Field()
    CoolerMaxHeight = Field()
    Colour = Field()
    FanPorts = Field()
    Height= Field()
    Width = Field()
    Depth = Field()
    Volume = Field()
    Weight = Field()
