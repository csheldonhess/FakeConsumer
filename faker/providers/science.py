from __future__ import unicode_literals
from . import BaseProvider

# create new provider class
class Provider(BaseProvider):
    word_list = ('abiosis', 'abrade', 'absorption', 'acceleration', 'accumulation', 
		'acid', 'acidic', 'activist', 'adaptation', 'agonistic', 'agrarian', 'airborne', 
		'alchemist', 'alignment', 'allele', 'alluvial', 'alveoli', 'ambiparous', 
		'amphibian', 'amplitude', 'analysis', 'ancestor', 'anodize', 'anomaly', 
		'anther', 'antigen', 'apiary', 'apparatus', 'application', 'approximation', 
		'aquatic', 'aquifer', 'arboreal', 'archeology', 'artery', 'assessment', 
		'asteroid', 'atmosphere', 'atomic', 'atrophy', 'attenuate', 'aven', 'aviary', 
		'axis', 'bacteria', 'balance', 'bases', 'biome', 'biosphere', 'black hole', 
		'blight', 'buoyancy', 'calcium', 'canopy', 'capacity', 'capillary', 'carapace', 
		'carcinogen', 'catalyst', 'cauldron', 'celestial', 'cells', 'centigrade', 
		'centimeter', 'centrifugal', 'chemical reaction', 'chemicals', 'chemistry', 
		'chlorophyll', 'choked', 'chromosome', 'chronic', 'churn', 'classification', 
		'climate', 'cloud', 'comet', 'composition', 'compound', 'compression', 
		'condensation', 'conditions', 'conduction', 'conductivity', 'conservation', 
		'constant', 'constellation', 'continental', 'convection', 'convention', 'cool', 
		'core', 'cosmic', 'crater', 'creature', 'crepuscular', 'crystals', 'cycle', 'cytoplasm', 
		'dampness', 'data', 'decay', 'decibel', 'deciduous', 'defoliate', 'density', 
		'denude', 'dependency', 'deposits', 'depth', 'desiccant', 'detritus', 
		'development', 'digestible', 'diluted', 'direction', 'disappearance', 'discovery', 
		'dislodge', 'displace', 'dissection', 'dissolution', 'dissolve', 'distance', 
		'diurnal', 'diverse', 'doldrums', 'dynamics', 'earthquake', 'eclipse', 'ecology', 
		'ecosystem', 'electricity', 'elements', 'elevation', 'embryo', 'endangered', 
		'endocrine', 'energy', 'entropy', 'environment', 'enzyme', 'epidermis', 'epoch', 
		'equilibrium', 'equine', 'erosion', 'essential', 'estuary', 'ethical', 'evaporation', 
		'event', 'evidence', 'evolution', 'examination', 'existence', 'expansion', 
		'experiment', 'exploration ', 'extinction', 'extreme', 'facet', 'fault', 'fauna', 
		'feldspar', 'fermenting', 'fission', 'fissure', 'flora', 'flourish', 'flowstone', 
		'foliage', 'food chain', 'forage', 'force', 'forecast', 'forensics', 'formations', 
		'fossil fuel', 'frequency', 'friction', 'fungi', 'fusion', 'galaxy', 'gastric', 
		'geo-science', 'geothermal', 'germination', 'gestation', 'global', 'gravitation', 
		'green', 'greenhouse effect', 'grotto', 'groundwater', 'habitat', 'heat', 'heavens', 
		'hemisphere', 'hemoglobin', 'herpetologist', 'hormones', 'host', 'humidity', 'hyaline', 
		'hydrogen', 'hydrology', 'hypothesis', 'ichthyology', 'illumination', 'imagination', 
		'impact of', 'impulse', 'incandescent', 'indigenous', 'inertia', 'inevitable', 'inherit', 
		'inquiry', 'insoluble', 'instinct', 'instruments', 'integrity', 'intelligence', 
		'interacts with', 'interdependence', 'interplanetary', 'invertebrate', 'investigation', 
		'invisible', 'ions', 'irradiate', 'isobar', 'isotope', 'joule', 'jungle', 'jurassic', 
		'jutting', 'kilometer', 'kinetics', 'kingdom', 'knot', 'laser', 'latitude', 'lava', 
		'lethal', 'life', 'lift', 'light', 'limestone', 'lipid', 'lithosphere', 'load', 
		'lodestone', 'luminous', 'luster', 'magma', 'magnet', 'magnetism', 'mangrove', 'mantle', 
		'marine', 'marsh', 'mass', 'matter', 'measurements', 'mechanical', 'meiosis', 'meridian', 
		'metamorphosis', 'meteor', 'microbes', 'microcosm', 'migration', 'millennia', 'minerals', 
		'modulate', 'moisture', 'molecule', 'molten', 'monograph', 'monolith', 'motion', 
		'movement', 'mutant', 'mutation', 'mysterious', 'natural', 'navigable', 'navigation', 
		'negligence', 'nervous system', 'nesting', 'neutrons', 'niche', 'nocturnal', 
		'nuclear energy', 'numerous', 'nurture', 'obsidian', 'ocean', 'oceanography', 'omnivorous', 
		'oolites (cave pearls)', 'opaque', 'orbit', 'organ', 'organism', 'ornithology', 
		'osmosis', 'oxygen', 'paleontology', 'parallax', 'particle', 'penumbra', 
		'percolate', 'permafrost', 'permutation', 'petrify', 'petrograph', 'phenomena', 
		'physical property', 'planetary', 'plasma', 'polar', 'pole', 'pollination', 
		'polymer', 'population', 'precipitation', 'predator', 'prehensile', 'preservation', 
		'preserve', 'pressure', 'primate', 'pristine', 'probe', 'process', 'propagation', 
		'properties', 'protected', 'proton', 'pulley', 'qualitative data', 'quantum', 'quark', 
		'quarry', 'radiation', 'radioactivity', 'rain forest', 'ratio', 'reaction', 'reagent', 
		'realm', 'redwoods', 'reeds', 'reflection', 'refraction', 'relationships between', 'reptile', 
		'research', 'resistance', 'resonate', 'rookery', 'rubble', 'runoff', 'salinity', 'sandbar', 
		'satellite', 'saturation', 'scientific investigation', 'scientist\'s', 'sea floor', 'season', 
		'sedentary', 'sediment', 'sedimentary', 'seepage', 'seismic', 'sensors', 'shard', 
		'similarity', 'solar', 'soluble', 'solvent', 'sonic', 'sound', 'source', 'species', 
		'spectacular', 'spectrum', 'speed', 'sphere', 'spring', 'stage', 'stalactite', 
		'stalagmites', 'stimulus', 'substance', 'subterranean', 'sulfuric acid', 'surface', 
		'survival', 'swamp', 'sylvan', 'symbiosis', 'symbol', 'synergy', 'synthesis', 'taiga', 
		'taxidermy', 'technology', 'tectonics', 'temperate', 'temperature', 'terrestrial', 
		'thermals', 'thermometer', 'thrust', 'torque', 'toxin', 'trade winds', 'pterodactyl',
		'transformation tremors', 'tropical', 'umbra', 'unbelievable', 'underwater', 'unearth', 
		'unique', 'unite', 'unity', 'universal', 'unpredictable', 'unusual', 'ursine', 'vacuole', 
		'valuable', 'vapor', 'variable', 'variety', 'vast', 'velocity', 'ventifact', 'verdant', 
		'vespiary', 'viable', 'vibration', 'virus', 'viscosity', 'visible', 'vista', 'vital', 
		'vitreous', 'volt', 'volume', 'vulpine', 'wave', 'wax', 'weather', 'westerlies', 'wetlands', 
		'whitewater', 'xeriscape', 'xylem', 'yield', 'zero-impact', 'zone', 'zygote', 'achieving', 
		'acquisition of', 'an alternative', 'analysis of', 'approach toward', 'area', 'aspects of', 
		'assessment of', 'assuming', 'authority', 'available', 'benefit of', 'circumstancial', 
		'commentary', 'components', 'concept of', 'consistent', 'corresponding', 'criteria', 
		'data', 'deduction', 'demonstrating', 'derived', 'distribution', 'dominant', 'elements', 
		'equation', 'estimate', 'evaluation', 'factors', 'features', 'final', 'function', 
		'initial', 'instance ', 'interpretation of', 'maintaining ', 'method', 'perceived', 
		'percent', 'period', 'positive', 'potential', 'previous', 'primary', 'principle', 
		'procedure', 'process', 'range', 'region', 'relevant', 'required', 'research', 
		'resources', 'response', 'role', 'section', 'select', 'significant ', 'similar', 
		'source', 'specific', 'strategies', 'structure', 'theory', 'transfer', 'variables',
        'corvidae', 'passerine', 'Pica pica', 'Chinchilla lanigera', 'Nymphicus hollandicus', 
        'Melopsittacus undulatus', )


    def scienceword(cls):
        """
        :example 'Lorem'
        """
        return cls.random_element(cls.word_list)


    def sciencewords(cls, nb=3):
        """
        Generate an array of random words
        :example array('Lorem', 'ipsum', 'dolor')
        :param nb how many words to return
        """
        return [cls.scienceword() for _ in range(0, nb)]


    def sciencesentence(cls, nb_words=6, variable_nb_words=True):
        """
        Generate a random sentence
        :example 'Lorem ipsum dolor sit amet.'
        :param nb_words around how many words the sentence should contain
        :param variable_nb_words set to false if you want exactly $nbWords returned,
            otherwise $nbWords may vary by +/-40% with a minimum of 1
        """
        if nb_words <= 0:
            return ''

        if variable_nb_words:
            nb_words = cls.randomize_nb_elements(nb_words)

        words = cls.sciencewords(nb_words)
        words[0] = words[0].title()

        return " ".join(words) + '.'

    def sciencesentences(cls, nb=3):
        """
        Generate an array of sentences
        :example array('Lorem ipsum dolor sit amet.', 'Consectetur adipisicing eli.')
        :param nb how many sentences to return
        :return list
        """
        return [cls.sciencesentence() for _ in range(0, nb)]


    def scienceparagraph(cls, nb_sentences=3, variable_nb_sentences=True):
        """
        Generate a single paragraph
        :example 'Sapiente sunt omnis. Ut pariatur ad autem ducimus et. Voluptas rem voluptas sint modi dolorem amet.'
        :param nb_sentences around how many sentences the paragraph should contain
        :param variable_nb_sentences set to false if you want exactly $nbSentences returned,
            otherwise $nbSentences may vary by +/-40% with a minimum of 1
        :return string
        """
        if nb_sentences <= 0:
            return ''

        if variable_nb_sentences:
            nb_sentences = cls.randomize_nb_elements(nb_sentences)

        return " ".join(cls.sciencesentences(nb_sentences))


    def scienceparagraphs(cls, nb=3):
        """
        Generate an array of paragraphs
        :example array($paragraph1, $paragraph2, $paragraph3)
        :param nb how many paragraphs to return
        :return array
        """
        return [cls.scienceparagraph() for _ in range(0, nb)]


    def sciencetext(cls, max_nb_chars=200):
        """
        Generate a text string.
        Depending on the $maxNbChars, returns a string made of words, sentences, or paragraphs.
        :example 'Sapiente sunt omnis. Ut pariatur ad autem ducimus et. Voluptas rem voluptas sint modi dolorem amet.'
        :param max_nb_chars Maximum number of characters the text should contain (minimum 5)
        :return string
        """
        text = []
        if max_nb_chars < 5:
            raise ValueError('text() can only generate text of at least 5 characters')

        if max_nb_chars < 25:
            # join words
            while not text:
                size = 0
                # determine how many words are needed to reach the $max_nb_chars once;
                while size < max_nb_chars:
                    word = (' ' if size else '') + cls.scienceword()
                    text.append(word)
                    size += len(word)
                text.pop()
            text[0] = text[0][0].upper() + text[0][1:]
            last_index = len(text) - 1
            text[last_index] += '.'
        elif max_nb_chars < 100:
            # join sentences
            while not text:
                size = 0
                # determine how many sentences are needed to reach the $max_nb_chars once
                while size < max_nb_chars:
                    sentence = (' ' if size else '') + cls.sciencesentence()
                    text.append(sentence)
                    size += len(sentence)
                text.pop()
        else:
            # join paragraphs
            while not text:
                size = 0
                # determine how many paragraphs are needed to reach the $max_nb_chars once
                while size < max_nb_chars:
                    paragraph = ('\n' if size else '') + cls.scienceparagraph()
                    text.append(paragraph)
                    size += len(paragraph)
                text.pop()

        return "".join(text)

#fake.add_provider(ScienceProvider)