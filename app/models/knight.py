from app.models.equipment import Equipment, Potion

class Knight:
    def __init__(self, config: dict):
        self.name = config["name"]
        self.base_hp = config["hp"]
        self.base_power = config["power"]
        
        # Cargar equipo
        self.weapon = Equipment(config["weapon"]["name"], power=config["weapon"]["power"])
        self.armour = [Equipment(a["part"], prot=a["protection"]) for a in config["armour"]]
        self.potion = Potion(config["potion"]["name"], config["potion"]["effect"]) if config["potion"] else None
        
        # Estadísticas finales calculadas
        self.hp = 0
        self.power = 0
        self.protection = 0
        self._prepare_for_battle()

    def _prepare_for_battle(self):
        """Aplica todas las bonificaciones antes del combate."""
        self.hp = self.base_hp
        self.power = self.base_power
        self.protection = sum(a.protection for a in self.armour)
        
        # Aplicar arma
        self.power += self.weapon.power
        
        # Aplicar poción
        if self.potion:
            self.hp += self.potion.hp
            self.power += self.potion.power
            self.protection += self.potion.protection

    def receive_damage(self, opponent_power: int):
        """Calcula el daño recibido y asegura que el HP no baje de 0."""
        damage = opponent_power - self.protection
        if damage > 0:
            self.hp = max(0, self.hp - damage)
