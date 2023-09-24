from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (Updater,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackQueryHandler
)
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater('5582099194:AAEmYEOCk9J6ynEpuFwqFF2t5QclxiJkHkM')
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    menu(update, context)


def menu (update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Парк", callback_data="PARK_START"),
            InlineKeyboardButton("Стрит", callback_data="STRIT_START"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Выберите направление", reply_markup=reply_markup)

def start_back (update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Парк", callback_data="PARK_START"),
            InlineKeyboardButton("Стрит", callback_data="STRIT_START"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Выберите напраление", reply_markup=reply_markup
    )







def details_p(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("Дека", callback_data='2'),
            InlineKeyboardButton("Руль", callback_data='3')
        ],

        [
            InlineKeyboardButton("Вилка", callback_data='4'),
            InlineKeyboardButton("Зажим", callback_data='5')
        ],

        [
            InlineKeyboardButton("Колеса", callback_data='6'),
            InlineKeyboardButton("Грипсы", callback_data='7')
        ],

        [
            InlineKeyboardButton("Рулевая", callback_data='8'),
        ],

        [
            InlineKeyboardButton("Наждак", callback_data='9'),
        ],
        [
            InlineKeyboardButton("Назад", callback_data='10'),
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Выберите запчасть", reply_markup=reply_markup
    )


def details_s(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Дека", callback_data='11'),
            InlineKeyboardButton("Руль", callback_data='12')
        ],


        [
            InlineKeyboardButton("Вилка", callback_data='13'),
            InlineKeyboardButton("SCS", callback_data='14')
        ],

        [
            InlineKeyboardButton("Колеса", callback_data='15'),
            InlineKeyboardButton("Наждак", callback_data='16')
        ],

        [
            InlineKeyboardButton("Рулевая", callback_data='17'),
            InlineKeyboardButton("Грипсы", callback_data='18')
        ],

        [
            InlineKeyboardButton("Назад", callback_data='19'),
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Выберите запчасть", reply_markup=reply_markup
    )        


def park_rudders_firms(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Blunt", callback_data='20'),
    InlineKeyboardButton("Ethic", callback_data='21')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='22'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите фирму руля", reply_markup=reply_markup
    )

def park_soundboards_firms(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Ethic", callback_data='23'),
    InlineKeyboardButton("Lucky", callback_data='24')
    ], 
    [
    InlineKeyboardButton("Core", callback_data='25'),
    ],
    [
    InlineKeyboardButton("Назад", callback_data='26'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите фирму деки", reply_markup=reply_markup
    )


def park_fork_firms(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Striker ", callback_data='27'),
    InlineKeyboardButton("North ", callback_data='28')
    ], 
    [
    InlineKeyboardButton("Ethic ", callback_data='29'),
    InlineKeyboardButton("Longway ", callback_data='30')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='31'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите фирму вилки", reply_markup=reply_markup
    ) 

def park_wheels_firms(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Striker", callback_data='32'),
    InlineKeyboardButton("Blunt", callback_data='33')
    ], 
    [
    InlineKeyboardButton("Movino", callback_data='34'),
    ], 
    [
    InlineKeyboardButton("Native", callback_data='35'),
    InlineKeyboardButton("Rideo", callback_data='36')
    ],  
    [
    InlineKeyboardButton("Назад", callback_data='37'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите фирму колёс", reply_markup=reply_markup
    ) 


def park_clamp_firms(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Ethic", callback_data='38'),
    InlineKeyboardButton("Native", callback_data='39')
    ], 
    [
    InlineKeyboardButton("Longway", callback_data='40'),
    InlineKeyboardButton("Movino", callback_data='41')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='42'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите зажим", reply_markup=reply_markup
    )

def flus_firms(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Striker ", callback_data='43'),
    InlineKeyboardButton("Tilt ", callback_data='44')
    ], 
    [
    InlineKeyboardButton("Ethic ", callback_data='45')
    ], 
    [
    InlineKeyboardButton("Movino ", callback_data='46'),
    InlineKeyboardButton("Hipe ", callback_data='47')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='48'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите фирму грипс", reply_markup=reply_markup
    )  


def emery_firms(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Ethic", callback_data='49'),
    InlineKeyboardButton("Axel", callback_data='50')
    ], 
    [
    InlineKeyboardButton("Jessup", callback_data='51'),
    InlineKeyboardButton("Chubby", callback_data='52')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='53'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите фирму наждака", reply_markup=reply_markup
    )  

def steering_firms(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Ethic", callback_data='54'),
    InlineKeyboardButton("Tilt", callback_data='55')
    ],
    [
    InlineKeyboardButton("Chubby", callback_data='56'),
    ],  
    [
    InlineKeyboardButton("Назад", callback_data='57'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите фирму рулевой", reply_markup=reply_markup
    ) 


def strit_soundboard_firms(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Tilt", callback_data='58'),
    InlineKeyboardButton("Ethic", callback_data='59')
    ],
    [
    InlineKeyboardButton("Native", callback_data='60'),
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='61'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите фирму деки", reply_markup=reply_markup
    )

def strit_ruders_firms(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Ethic", callback_data='62'),
    InlineKeyboardButton("Tilt", callback_data='63')
    ],
    [
    InlineKeyboardButton("Axel", callback_data='64'),
    InlineKeyboardButton("Native", callback_data='65')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='66'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите фирму руля", reply_markup=reply_markup
    )

def strit_forks_firms(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Native", callback_data='67'),
    InlineKeyboardButton("Tilt ", callback_data='68')
    ], 
    [
    InlineKeyboardButton("Axel ", callback_data='69'),
    InlineKeyboardButton("Striker ", callback_data='70')
    ], 
    [
    InlineKeyboardButton("Lucky ", callback_data='71'),
    InlineKeyboardButton("Ethic ", callback_data='72')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='73'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите фирму вилки", reply_markup=reply_markup
    )

def SCS_firms(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Native ", callback_data='74'),
    InlineKeyboardButton("Tilt ", callback_data='75')
    ], 
    [
    InlineKeyboardButton("Striker ", callback_data='76'),
    InlineKeyboardButton("Axel ", callback_data='77')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='78'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите фирму SCS", reply_markup=reply_markup
    )



def strit_wheels_firms(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Tilt", callback_data='79'),
    InlineKeyboardButton("River", callback_data='80')
    ], 
    [
    InlineKeyboardButton("Native", callback_data='81'),
    InlineKeyboardButton("Striker", callback_data='82')
    ],
    [
    InlineKeyboardButton("Blunt", callback_data='83'),
    InlineKeyboardButton("Ethic", callback_data='84')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='85'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите фирму колёс", reply_markup=reply_markup
    )


def park_rudders_blunt(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Blunt Reaper V2", callback_data='86'),
    InlineKeyboardButton("Blunt Reaper V3", callback_data='87')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='back'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите руль", reply_markup=reply_markup
    )

def park_rudders_ethic(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [ 
    [
    InlineKeyboardButton("Ethic Dryde", callback_data='Dryde'),
    InlineKeyboardButton("Ethic Dynasty V2", callback_data='Dynasty')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='back'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите руль", reply_markup=reply_markup
    )

def park_soundboard_ethic(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Ethic Pandemonium", callback_data='88'),
    InlineKeyboardButton("Ethic Pandora", callback_data='89')
    ], 
    [
    InlineKeyboardButton("Ethic Erawan", callback_data='90'),
    InlineKeyboardButton("Ethic Vulcain", callback_data='91')
    ], 
    [
    InlineKeyboardButton("Ethic Vulcain V2", callback_data='92'),
    InlineKeyboardButton("Ethic Ethic Erawan V2", callback_data='93')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='94'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите деку", reply_markup=reply_markup
    ) 

def park_soundboard_core(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Core SL1", callback_data='95'),
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='96'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите вилку", reply_markup=reply_markup
    )  

def park_soundboards_lucky(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Lucky Prospect 2022", callback_data='97'),
    InlineKeyboardButton("Lucky Prospect 2021", callback_data='98')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='99'),
    ],

    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите деку", reply_markup=reply_markup
    ) 



def park_fork_striker(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Striker Lux", callback_data='100'),
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='101'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите вилку", reply_markup=reply_markup
    ) 

def park_fork_ethic(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Ethic Legion", callback_data='102'),
    ],
    [
    InlineKeyboardButton("Назад", callback_data='103'),
    ],  
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите вилку", reply_markup=reply_markup
    ) 

def park_fork_north(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("North Amber", callback_data='104')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='105'),
    ],   
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите вилку", reply_markup=reply_markup
    ) 

def park_fork_longway(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [ 
    [
    InlineKeyboardButton("Longway Hapria", callback_data='106')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='107'),
    ],  
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите вилку", reply_markup=reply_markup
    )  





def park_wheels_movino(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Movino Slave", callback_data='108'),
    ],
    [
    InlineKeyboardButton("Назад", callback_data='109'),
    ],  
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите колеса", reply_markup=reply_markup
    ) 

def park_wheels_native(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Native Stem Pro", callback_data='110'), 
    ],
    [
    InlineKeyboardButton("Назад", callback_data='111'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите колеса", reply_markup=reply_markup
    ) 

def park_wheels_striker(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Striker Lux", callback_data='112'),
    InlineKeyboardButton("Striker Gravis", callback_data='113')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='114'),
    ],   
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите колеса", reply_markup=reply_markup
    ) 

def park_wheels_rideo(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [ 
    [
    InlineKeyboardButton("Rideo Full Core", callback_data='115'),
    InlineKeyboardButton("Rideo Classic", callback_data='116')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='117')
    ] 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите колеса", reply_markup=reply_markup
    )    

def park_wheels_blunt(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Blunt Wheel", callback_data='118'),
    InlineKeyboardButton("Blunt S3", callback_data='119')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='120'),
    ],  
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите колеса", reply_markup=reply_markup
    )   





def park_clamp_ethic(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Ethic Sylphe", callback_data='121'),
    ],
    [
    InlineKeyboardButton("Назад", callback_data='122'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите зажим", reply_markup=reply_markup
    ) 

def park_clamp_movino(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Movino Kraken", callback_data='123')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='124'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите зажим", reply_markup=reply_markup
    ) 

def park_clamp_longway(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [ 
    [
    InlineKeyboardButton("Longway Pracinct", callback_data='125'),
    ],
    [
    InlineKeyboardButton("Назад", callback_data='126'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите зажим", reply_markup=reply_markup
    ) 

def park_clamp_native(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Native Orca", callback_data='127')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='128'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите зажим", reply_markup=reply_markup
    ) 





def flus_tilt(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Tilt Topo Grip", callback_data='129'),
    InlineKeyboardButton("Tilt Metra", callback_data='130')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='131'),
    ],  
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите грипсы", reply_markup=reply_markup
    ) 

def flus_hipe(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Hipe H4", callback_data='132')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='133'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите грипсы", reply_markup=reply_markup
    ) 

def flus_movino(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Movino Elite", callback_data='134'),
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='135')
    ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите грипсы", reply_markup=reply_markup
    ) 

def flus_ethic(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [ 
    [
    InlineKeyboardButton("Ethic DTC", callback_data='136')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='137')
    ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите грипсы", reply_markup=reply_markup
    ) 



def flus_striker(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Striker Logo", callback_data='138')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='139')
    ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите грипсы", reply_markup=reply_markup
    )   




def emery_ethic(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Ethic Classic", callback_data='140'),
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='141'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите наждак", reply_markup=reply_markup
    )    

def emery_axel(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Axel Classic", callback_data='142')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='143'),
    ],  
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите наждак", reply_markup=reply_markup
    ) 

def emery_jessup(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [ 
    [
    InlineKeyboardButton("Jessup 9", callback_data='144'),
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='145'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите наждак", reply_markup=reply_markup
    ) 

def emery_chubby(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Chubby Burger", callback_data='146')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='147'),
    ],  
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите наждак", reply_markup=reply_markup
    ) 




def steering_ethic(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Ethic Silcone", callback_data='148'),
    InlineKeyboardButton("Ethic DTC", callback_data='149')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='150'),
    ],  
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите рулевую", reply_markup=reply_markup
    ) 

def steering_tilt(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Tilt Integrated", callback_data='151')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='152'),
    ],  
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите рулевую", reply_markup=reply_markup
    ) 

def steering_chubby(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Chubby Donut", callback_data='153'),
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='154'),
    ],  
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите рулевую", reply_markup=reply_markup
    ) 







def strit_soundboard_ethic(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Ethic Lindworm V3", callback_data='155')
    ], 
    [
    InlineKeyboardButton("Ethic Lindworm V4", callback_data='156'),
    InlineKeyboardButton("Ethic Vulcain Boxed", callback_data='157')
    ], 
    [
    InlineKeyboardButton("Ethic Vulcain V2 Boxed", callback_data='158'),
    InlineKeyboardButton("Ethic Pandora", callback_data='159')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='160'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите деку", reply_markup=reply_markup
    )

def strit_soundboard_tilt(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Tilt Formula", callback_data='161'),
    InlineKeyboardButton("Tilt Stage One", callback_data='162')
    ],
    [
    InlineKeyboardButton("Tilt Theory", callback_data='153')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='154'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите деку", reply_markup=reply_markup
    )

def strit_soundboard_native(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Native Stem", callback_data='155'),
    InlineKeyboardButton("Native Advent", callback_data='156'),
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='157'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите деку", reply_markup=reply_markup
    )



def strit_ruders_ethic(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Ethic Trianon", callback_data='158'),
    InlineKeyboardButton("Ethic Tenasity", callback_data='159')
    ], 
    [
    InlineKeyboardButton("Ethic Deildegast", callback_data='160'),
    ],
    [
    InlineKeyboardButton("Назад", callback_data='161'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите руль", reply_markup=reply_markup
    )

def strit_ruders_tilt(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Tilt Stage One", callback_data='162')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='163'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите руль", reply_markup=reply_markup
    )

def strit_ruders_axel(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Axel Classic", callback_data='164'),
    ],
    [
    InlineKeyboardButton("Назад", callback_data='165'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите руль", reply_markup=reply_markup
    )


def strit_ruders_native(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [ 
    [
    InlineKeyboardButton("Native Stem", callback_data='166')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='167'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите руль", reply_markup=reply_markup
    )




def strit_forks_lucky(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Lucky Huracan", callback_data='168'),
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='169'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите вилку", reply_markup=reply_markup
    )

def strit_forks_striker(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Striker Gravis", callback_data='170')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='171'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите вилку", reply_markup=reply_markup
    )

def strit_forks_axel(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [ 
    [
    InlineKeyboardButton("Axel Top Gun", callback_data='172'),
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='173'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите вилку", reply_markup=reply_markup
    )

def strit_forks_ethic(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [ 
    [
    InlineKeyboardButton("Ethic Merrow", callback_data='174'),
    InlineKeyboardButton("Ethic Legion", callback_data='175')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='176'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите вилку", reply_markup=reply_markup
    )

def strit_forks_native(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Native Stem", callback_data='177'),
    InlineKeyboardButton("Native Flomengo", callback_data='178'),
    ],
    [
    InlineKeyboardButton("Назад", callback_data='179'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите вилку", reply_markup=reply_markup
    )


def strit_forks_tilt(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Tilt Stage One", callback_data='180'),
    InlineKeyboardButton("Tilt Tomahawk", callback_data='181')
    ],
    [
    InlineKeyboardButton("Tilt Regit", callback_data='182')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='183'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите вилку", reply_markup=reply_markup
    )







def SCS_native(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Native Stem", callback_data='184'),
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='185'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите SCS", reply_markup=reply_markup
    )

def SCS_tilt(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Tilt Stage One", callback_data='186'),
    InlineKeyboardButton("Tilt Classic", callback_data='187')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='188'),
    ],  
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите SCS", reply_markup=reply_markup
    )

def SCS_striker(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Striker Gravis", callback_data='189')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='190'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите SCS", reply_markup=reply_markup
    )


def SCS_axel(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [ 
    [
    InlineKeyboardButton("Axel Diamond", callback_data='191'),
    InlineKeyboardButton("Axel Raptor", callback_data='192')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='193'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите SCS", reply_markup=reply_markup
    )



def strit_wheels_striker(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [ 
    [
    InlineKeyboardButton("Striker Gravis", callback_data='194')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='195'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите колеса", reply_markup=reply_markup
    )

def strit_wheels_ethic(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Ethic Mogway", callback_data='196'),
    InlineKeyboardButton("Ethic Incube V2", callback_data='197')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='198'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите колеса", reply_markup=reply_markup
    )



def strit_wheels_blunt(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Blunt Tri", callback_data='199'),
    ],
    [
    InlineKeyboardButton("Назад", callback_data='200'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите колеса", reply_markup=reply_markup
    )



def strit_wheels_native(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [ 
    [
    InlineKeyboardButton("Native Stem Pro", callback_data='201'),
    ],
    [
    InlineKeyboardButton("Назад", callback_data='202'),
    ], 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите колеса", reply_markup=reply_markup
    )


def strit_wheels_river(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("River Rapids", callback_data='203')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='204')
    ] 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите колеса", reply_markup=reply_markup
    )


def strit_wheels_tilt(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Tilt Stage One", callback_data='205'),
    InlineKeyboardButton("Tilt UHR", callback_data='206')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='207')
    ] 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Выберите колеса", reply_markup=reply_markup
    )




def park_rudders_reaper_V2(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Беру", callback_data='209')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='Back'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Стоимость: 2390грн. Вес: 818гр", reply_markup=reply_markup
    )

def park_rudders_reaper_V3(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Беру", callback_data='210')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='Back'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Стоимость: 2800грн. Вес: 930гр", reply_markup=reply_markup
    )

def park_rudders_dryde(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Беру", callback_data='210')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='Back'),
    ] 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Стоимость: 1799грн. Вес: 740гр", reply_markup=reply_markup
    )

def park_rudders_dynasty(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Беру", callback_data='211')
    ],
    [
    InlineKeyboardButton("Назад", callback_data='Back'),
    ] 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Стоимость: 2200грн. Вес: 1018гр", reply_markup=reply_markup
    )



def park_soundboard_core(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Беру", callback_data='212')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='Back'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Стоимость: 3599грн. Вес: 1345гр", reply_markup=reply_markup
    )

def park_soundboard_panda(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Беру", callback_data='213')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='Back'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Стоимость: 6300грн. Вес: 1260гр", reply_markup=reply_markup
    )

def park_soundboard_pandora(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Беру", callback_data='214')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='Back'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Стоимость: 4500грн. Вес: 1300гр", reply_markup=reply_markup
    )

def park_soundboard_erawan(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Беру", callback_data='215')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='Back'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Стоимость: 2800грн. Вес: 1260гр", reply_markup=reply_markup
    )

def park_soundboard_vulcain(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Беру", callback_data='216')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='Back'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Стоимость: 4200грн. Вес: 1300гр", reply_markup=reply_markup
    )

def park_soundboard_vulcain_V2(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Беру", callback_data='217')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='Back'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Стоимость: 4800грн. Вес: 1300гр", reply_markup=reply_markup
    )

def park_soundboard_erawan_V2(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Беру", callback_data='218')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='Back'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Стоимость: 4500грн. Вес: 1250гр", reply_markup=reply_markup
    )

def park_soundboard_prospect_22(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Беру", callback_data='219')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='Back'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Стоимость: 4200грн. Вес: 1270гр", reply_markup=reply_markup
    )

def park_soundboard_prospect_21(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Беру", callback_data='220')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='Back'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Стоимость: 4150грн. Вес: 1333гр", reply_markup=reply_markup
    )


def park_fork_striker(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
    [
    InlineKeyboardButton("Беру", callback_data='221')
    ], 
    [
    InlineKeyboardButton("Назад", callback_data='Back'),
    ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
    text="Стоимость: 4150грн. Вес: 1333гр", reply_markup=reply_markup
    )





def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    match query.data:
        case "PARK_START":
            details_p(update, context)
        case "STRIT_START":
            details_s(update, context)


        case "2":
            park_soundboards_firms(update, context)
        case "3":
            park_rudders_firms(update, context)
        case "4":
            park_fork_firms(update, context)
        case "5":
            park_clamp_firms(update, context)  
        case "6": 
            park_wheels_firms(update, context)
        case "7": 
            flus_firms(update, context)
        case "8": 
            steering_firms(update, context)
        case "9": 
            emery_firms(update, context)
        case "10": 
            start_back(update, context)


        case "11": 
            strit_soundboard_firms(update, context)
        case "12": 
            strit_ruders_firms(update, context)
        case "13": 
           strit_forks_firms(update, context)
        case "14": 
           SCS_firms(update, context)
        case "15": 
           strit_wheels_firms(update, context)
        case "16": 
            emery_firms(update, context)
        case "17": 
            steering_firms(update, context)
        case "18": 
          flus_firms(update, context)
        case "19": 
          start_back(update, context) 


        case "20": 
            park_rudders_blunt(update, context)
        case "21": 
            park_rudders_ethic(update, context)
        case "22": 
            details_p(update, context)

        case "23": 
            park_soundboard_ethic(update, context)
        case "24": 
            park_soundboards_lucky(update, context)
        case "25": 
            park_soundboard_core(update, context)
        case "26": 
            details_p(update, context) 

        case "27": 
            park_fork_striker(update, context)
        case "28": 
            park_fork_north(update, context)
        case "29": 
            park_fork_ethic(update, context)
        case "30": 
            park_fork_longway(update, context)
        case "31": 
            details_p(update, context)

        case "32": 
            park_wheels_striker(update, context)
        case "33": 
            park_wheels_blunt(update, context)
        case "34": 
            park_wheels_movino(update, context)
        case "35": 
            park_wheels_native(update, context)
        case "36": 
            park_wheels_rideo(update, context)  
        case "37": 
            details_p(update, context)

        case "38": 
            park_clamp_ethic(update, context)  
        case "39": 
            park_clamp_native(update, context)
        case "40": 
            park_clamp_longway(update, context)  
        case "41": 
            park_clamp_movino(update, context)
        case "42": 
            details_p(update, context) 

        case "43": 
            flus_striker(update, context)
        case "44": 
            flus_tilt(update, context)  
        case "45": 
            flus_ethic(update, context)
        case "46": 
            flus_movino(update, context)  
        case "47": 
            flus_hipe(update, context) 
        case "48": 
            details_p(update, context)  

        case "49": 
            emery_ethic(update, context)  
        case "50": 
            emery_axel(update, context)
        case "51": 
            emery_jessup(update, context)  
        case "52": 
            emery_chubby(update, context)
        case "53": 
            details_p(update, context) 

        case "54": 
            steering_ethic(update, context)  
        case "55": 
            steering_tilt(update, context)
        case "56": 
            steering_chubby(update, context)  
        case "57": 
            details_p(update, context)  

        case "58": 
            strit_soundboard_tilt(update, context)  
        case "59": 
            strit_soundboard_ethic(update, context)
        case "60": 
            strit_soundboard_native(update, context)  
        case "61": 
            details_s(update, context)   

        case "62": 
            strit_ruders_ethic(update, context)  
        case "63": 
            strit_ruders_tilt(update, context)
        case "64": 
            strit_ruders_axel(update, context)      
        case "65": 
            strit_ruders_native(update, context)  
        case "66": 
            details_s(update, context)      

        case "67": 
            strit_forks_native(update, context)
        case "68": 
            strit_forks_tilt(update, context)  
        case "69": 
            strit_forks_axel(update, context)
        case "70": 
            strit_forks_striker(update, context)      
        case "71":
            strit_forks_lucky(update, context) 
        case "72": 
            strit_forks_ethic(update, context)  
        case "73": 
            details_s(update, context) 

        case "74": 
            SCS_native(update, context)      
        case "75": 
            SCS_tilt(update, context) 
        case "76": 
            SCS_striker(update, context)
        case "77": 
            SCS_axel(update, context)  
        case "78": 
            details_s(update, context) 

        case "79": 
            strit_wheels_tilt(update, context)      
        case "80": 
            strit_wheels_river(update, context) 
        case "81": 
            strit_wheels_native(update, context)
        case "82": 
            strit_wheels_striker(update, context)      
        case "83": 
            strit_wheels_blunt(update, context) 
        case "84": 
            strit_wheels_ethic(update, context)
        case "85": 
            details_s(update, context)

        case "86": 
            park_rudders_reaper_V2(update, context)
        case "87": 
            park_rudders_reaper_V3(update, context) 
        case "back": 
            park_rudders_firms(update, context)         
        case "Dryde": 
            park_rudders_reaper_V2(update, context)
        case "Dynasty": 
            park_rudders_reaper_V3(update, context) 
        case "back": 
            park_rudders_firms(update, context) 

        case "88": 
            park_soundboard_panda(update, context) 
        case "89": 
            park_soundboard_pandora(update, context)         
        case "90": 
            park_soundboard_erawan(update, context)
        case "91": 
            park_soundboard_vulcain(update, context) 
        case "92": 
            park_soundboard_vulcain_V2(update, context) 
        case "93": 
            park_soundboard_erawan_V2(update, context) 
        case "94": 
            park_soundboards_firms(update, context)
        case "95": 
            park_soundboard_core(update, context)
        case "96": 
            park_soundboards_firms(update, context)
        case "97": 
            park_soundboards_firms(update, context)
        case "98": 
            park_soundboard_core(update, context)
        case "99": 
            park_soundboards_firms(update, context)



start_handler = CommandHandler('start', start)
button_handler = (CallbackQueryHandler(button))
dispatcher.add_handler(button_handler)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()
