import heapq

class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, nome):
        if nome not in self.vertices:
            self.vertices[nome] = []

    def adicionar_aresta(self, origem, destino, distancia):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)

       
        if destino not in [viz[0] for viz in self.vertices[origem]]:
            self.vertices[origem].append((destino, distancia))
        if origem not in [viz[0] for viz in self.vertices[destino]]:
            self.vertices[destino].append((origem, distancia))

    def dijkstra(self, origem, destino):
        distancias = {v: float('inf') for v in self.vertices}
        distancias[origem] = 0
        caminho = {}
        heap = [(0, origem)]
        visitados = set()

        while heap:
            dist_atual, atual = heapq.heappop(heap)
            if atual in visitados:
                continue
            visitados.add(atual)

            for vizinho, peso in self.vertices[atual]:
                nova_dist = dist_atual + peso
                if nova_dist < distancias[vizinho]:
                    distancias[vizinho] = nova_dist
                    caminho[vizinho] = atual
                    heapq.heappush(heap, (nova_dist, vizinho))


        rota = []
        atual = destino
        while atual != origem:
            rota.insert(0, atual)
            atual = caminho.get(atual)
            if atual is None:
                return None, float('inf')
        rota.insert(0, origem)

        return rota, distancias[destino]

def menu():
    grafo = Grafo()
    while True:
        print("\n🔹 MENU DE ROTAS 🔹")
        print("1. Adicionar cidade")
        print("2. Adicionar rota entre cidades")
        print("3. Calcular rota mais curta")
        print("4. Sair")
        opcao = input("Escolha uma opção (1–4): ").strip()

        if opcao == "1":
            cidade = input("Nome da cidade: ").strip()
            grafo.adicionar_vertice(cidade)
            print(f"✅ Cidade '{cidade}' adicionada.")

        elif opcao == "2":
            origem = input("Cidade de origem: ").strip()
            destino = input("Cidade de destino: ").strip()
            try:
                distancia = float(input("Distância entre elas (em km): ").strip())
                grafo.adicionar_aresta(origem, destino, distancia)
                print("✅ Rota adicionada com sucesso.")
            except ValueError:
                print("❌ Distância inválida. Use apenas números.")

        elif opcao == "3":
            origem = input("Cidade de origem: ").strip()
            destino = input("Cidade de destino: ").strip()

            if origem not in grafo.vertices or destino not in grafo.vertices:
                print("❌ Uma ou ambas as cidades não estão cadastradas.")
                continue

            rota, distancia_total = grafo.dijkstra(origem, destino)
            if rota:
                print(f"\n🚗 Melhor caminho: {' → '.join(rota)}")
                print(f"📏 Distância total: {distancia_total:.2f} km")
            else:
                print("❌ Não foi possível encontrar uma rota entre as cidades.")

        elif opcao == "4":
            print("🔚 Encerrando sistema. Até a próxima!")
            break

        else:
            print("❌ Opção inválida. Escolha de 1 a 4.")


if __name__ == "__main__":
    menu()