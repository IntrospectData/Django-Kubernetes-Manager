import factory
import factory.django.DjangoModelFactory as DMF
import factory.fuzzy
from faker import Faker

fake = Faker()

models_path = 'django_kubernetes_manager.models.'



class TargetClusterFactory(DMF):
    class Meta:
        model = models_path + 'TargetCluster'

    pass



class KubernetesContainerFactory(DMF):
    class Meta:
        model = models_path + 'KubernetesContainer'

    name = factory.fuzzy.FuzzyText(length=8, suffix="-container")
    description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True)
    cluster = factory.SubFactory(TargetClusterFactory)
    config = fake.pydict(nb_elements=4, variable_nb_elements=True)
    deployed = None
    deleted = None
    image_name = factory.fuzzy.FuzzyChoice(["debian", "alpine", "busybox"])
    image_tag = "latest"
    image_pull_policy = "IfNotPresent"
    command = "/bin/bash"
    args = "-c,sleep 6000"
    port = factory.fuzzy.FuzzyChoice([80, 8080, 8000])
    volume_mount = None



class KubernetesPodTemplateFactory(DMF):
    class Meta:
        model = models_path + 'KubernetesPodTemplate'

    name = factory.fuzzy.FuzzyText(length=8, suffix="-container")
    description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True)
    cluster = factory.SubFactory(TargetClusterFactory)
    config = fake.pydict(nb_elements=4, variable_nb_elements=True)
    deployed = None
    deleted = None
    labels = {"app": fake.word()}
    annotations = None
    volume = None
    primary_container = factory.SubFactory(KubernetesContainerFactory)
    secondary_container = None
    restart_policy = 'Always'



class KubernetesDeploymentFactory(DMF):
    class Meta:
        model = models_path + 'KubernetesDeployment'

    name = factory.fuzzy.FuzzyText(length=8, suffix="-container")
    description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True)
    cluster = factory.SubFactory(TargetClusterFactory)
    config = fake.pydict(nb_elements=4, variable_nb_elements=True)
    deployed = None
    deleted = None
    labels = {"app": fake.word()}
    annotations = None
    api_version = 'apps/v1'
    kind = 'Deployment'
    port = factory.fuzzy.FuzzyChoice([80, 8080, 8000])
    namespace = 'test'
    kuid = None
    selector = labels
    replicas = 1
    pod_template = factory.SubFactory(KubernetesPodTemplateFactory)



class KubernetesJobFactory(DMF):
    class Meta:
        model = models_path + 'KubernetesJob'

    name = factory.fuzzy.FuzzyText(length=8, suffix="-container")
    description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True)
    cluster = factory.SubFactory(TargetClusterFactory)
    config = fake.pydict(nb_elements=4, variable_nb_elements=True)
    deployed = None
    deleted = None
    labels = {"app": fake.word()}
    annotations = None
    api_version = 'apps/v1'
    kind = 'Deployment'
    port = factory.fuzzy.FuzzyChoice([80, 8080, 8000])
    namespace = 'test'
    kuid = None
    pod_template = factory.SubFactory(KubernetesPodTemplateFactory)
    backoff_limit = factory.fuzzy.FuzzyInteger(1, 10)
