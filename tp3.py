from owlready2 import get_ontology, sync_reasoner, default_world

onto = get_ontology("test.owl").load()
sync_reasoner()

all_persons = onto.search(type = onto.Person)

individuals_with_parents = onto.search(hasParent = "*")

print("All persons in the ontology:")
for person in all_persons:
    print(person.iri)

print("\nIndividuals with parents:")
for individual in individuals_with_parents:
    parents = [parent.iri for parent in individual.hasParent]
    print(f"{individual.iri} has parent(s): {parents}")

onto.save(file = "updated_test.owl")

print("\nRDF triples in the ontology:")
graph = default_world.as_rdflib_graph()
for subj, pred, obj in graph:
    print(subj, pred, obj)
