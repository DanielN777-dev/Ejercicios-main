class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre},{self.telefono}"
        


class AgendaContactos:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def agregar_contacto(self, contacto):
        with open(self.ruta_archivo, "a", encoding="utf-8") as f:
            f.write(str(contacto) + "\n")

    def listar_contactos(self):
        contactos = []
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        nombre, telefono = linea.split(",")
                        contactos.append(Contacto(nombre, telefono))
        except FileNotFoundError:
            print("Aún no hay contactos guardados.")
        return contactos

    def buscar_por_nombre(self, nombre):
        for c in self.listar_contactos():
            if c.nombre.lower() == nombre.lower():
                return c
        return None

    def eliminar_contacto(self, nombre):
        """RETO: elimina un contacto reescribiendo el archivo sin él."""
        contactos = self.listar_contactos()
        contactos_restantes = [c for c in contactos if c.nombre.lower() != nombre.lower()]

        with open(self.ruta_archivo, "w", encoding="utf-8") as f:
            for c in contactos_restantes:
                f.write(str(c) + "\n")

        eliminado = len(contactos) != len(contactos_restantes)
        print("Contacto eliminado." if eliminado else "No se encontró ese contacto.")


# --- Uso ---
agenda = AgendaContactos("contactos.txt")
agenda.agregar_contacto(Contacto("Ana", "555-1234"))
agenda.agregar_contacto(Contacto("Luis", "555-5678"))
agenda.agregar_contacto(Contacto("Maria", "555-9012"))
agenda.agregar_contacto(Contacto("Luis", "555-5678"))


agenda.eliminar_contacto("Ana")
for c in agenda.listar_contactos():
    print(c)