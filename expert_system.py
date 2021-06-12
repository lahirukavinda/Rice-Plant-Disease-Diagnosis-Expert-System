from experta import *
from IPython.display import Image, display
import time

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

class color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

def preprocess():
	global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
	diseases = open("diseases.txt")
	diseases_t = diseases.read()
	diseases_list = diseases_t.split("\n")
	diseases.close()
	for disease in diseases_list:
		disease_s_file = open("Disease symptoms/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		s_list = disease_s_data.split("\n")
		symptom_map[str(s_list)] = disease
		disease_s_file.close()
		disease_s_file = open("Disease descriptions/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_desc_map[disease] = disease_s_data
		disease_s_file.close()
		disease_s_file = open("Disease treatments/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_treatment_map[disease] = disease_s_data
		disease_s_file.close()

def get_details(disease):
	return d_desc_map[disease]

def get_treatments(disease):
	return d_treatment_map[disease]

def print_start() :
		print(color.BOLD)
		print("--------------------------------------------------------------------------------------------------------------------")
		print(" 8888888b.  8888888  .d8888b.  8888888888       8888888888 Y88b   d88P 8888888b.  8888888888 8888888b.  88888888888")
		print(" 888   Y88b   888   d88P  Y88b 888              888         Y88b d88P  888   Y88b 888        888   Y88b     888")
		print(" 888    888   888   888    888 888              888          Y88o88P   888    888 888        888    888     888")
		print(" 888   d88P   888   888        8888888          8888888       Y888P    888   d88P 8888888    888   d88P     888")
		print(" 8888888P\"    888   888        888              888           d888b    8888888P\"  888        8888888P\"      888")
		print(" 888 T88b     888   888    888 888              888          d88888b   888        888        888 T88b       888")
		print(" 888  T88b    888   Y88b  d88P 888              888         d88P Y88b  888        888        888  T88b      888")
		print(" 888   T88b 8888888  \"Y8888P\"  8888888888       8888888888 d88P   Y88b 888        8888888888 888   T88b     888")
		print("--------------------------------------------------------------------------------------------------------------------")
		print(color.END)
		time.sleep(2)
		print("Hi! I am " + color.BOLD + color.RED + "RICE EXPERT" + color.END + color.END +", I am here to help you make you to identify rice plant related diseases.")
		print("For that you'll have to answer a few questions about rice plant conditions")
		print(color.BOLD + "Do you see any of the following symptoms in rice plants?" + color.END)
		print("")
		time.sleep(2)

def print_details(id_disease, disease_details, treatments, prob) :
		display(Image(filename='images/' + id_disease + '.jpg'))
		if prob :
			print(color.BOLD + "The most probable disease that the rice plant have is" + color.END, end= "")
		else :
			print(color.BOLD + "With high uncertainity, we assume the disease that the rice plant have as" + color.END, end= "")
		print(color.BOLD + color.RED + " %s\n" %(id_disease) + color.END + color.END)
		print(color.BOLD + "A short description of the disease is given below :\n" + color.END)
		print(disease_details+"\n")
		print(color.BOLD + "The common treatment and procedures suggested by the experts are: \n" + color.END)
		print(treatments+"\n")

def if_not_matched(disease):
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		print_details(id_disease, disease_details, treatments, 0)

class Greetings(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print_start()
		yield Fact(action="find_disease")

	@Rule(Fact(action='find_disease'), NOT(Fact(g01=W())),salience = 1)
	def symptom_0(self):
		self.declare(Fact(g01=input(color.BOLD + color.BLUE + "Spots on the leaf midrib" + color.END + color.END + " (1-4) (yes/no): ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(g02=W())),salience = 1)
	def symptom_1(self):
		self.declare(Fact(g02=input(color.BOLD + color.BLUE + "Rhombus-shaped patches on leaves and leaf midribs" + color.END + color.END + " (P1) (yes/no): ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(g09=W())),salience = 1)
	def symptom_2(self):
		self.declare(Fact(g09=input(color.BOLD + color.BLUE + "Brown spots with midpoints are gray or white on the leaves" + color.END + color.END + " (P2) (yes/no): ")))       

	@Rule(Fact(action='find_disease'), NOT(Fact(g14=W())),salience = 1)
	def symptom_3(self):
		self.declare(Fact(g14=input(color.BOLD + color.BLUE + "The edges of the spot are reddish brown" + color.END + color.END + " (P3) (yes/no): ")))
        
	@Rule(Fact(action='find_disease'), NOT(Fact(g20=W())),salience = 1)
	def symptom_4(self):
		self.declare(Fact(g20=input(color.BOLD + color.BLUE + "Spots are grayish green" + color.END + color.END + " (P4-7): ")))
        
	@Rule(Fact(action='find_disease'), NOT(Fact(g27=W())),salience = 1)
	def symptom_5(self):
		self.declare(Fact(g27=input(color.BOLD + color.BLUE + "Spore balls are yellow, smooth and covered by membranes" + color.END + color.END + " (P5) (yes/no): ")))
        
	@Rule(Fact(action='find_disease'), NOT(Fact(g32=W())),salience = 1)
	def symptom_6(self):
		self.declare(Fact(g32=input(color.BOLD + color.BLUE + "A little panicle is produced" + color.END + color.END + " (P6-8) (yes/no): ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(g33=W())),salience = 1)
	def symptom_7(self):
		self.declare(Fact(g33=input(color.BOLD + color.BLUE + "Stunted plant growth" + color.END + color.END + " (P6-8) (yes/no): ")))    
        
	@Rule(Fact(action='find_disease'), NOT(Fact(g34=W())),salience = 1)
	def symptom_8(self):
		self.declare(Fact(g34=input(color.BOLD + color.BLUE + "Yellowish leaves with brown patches" + color.END + color.END + " (P6) (yes/no): ")))    

	@Rule(Fact(action='find_disease'), NOT(Fact(g38=W())),salience = 1)
	def symptom_9(self):
		self.declare(Fact(g38=input(color.BOLD + color.BLUE + "Wet lines on the edge of the leaf or wounded part of the leaf" + color.END + color.END + " (P7) (yes/no): ")))        

	@Rule(Fact(action='find_disease'), NOT(Fact(g43=W())),salience = 1)
	def symptom_10(self):
		self.declare(Fact(g43=input(color.BOLD + color.BLUE + "Sterile" + color.END + color.END + " (P8) (yes/no): ")))      
    
	@Rule(Fact(action='find_disease'),Fact(g01="yes"),Fact(g02="yes"))
	def disease_0(self):
		self.declare(Fact(disease="blast"))

	@Rule(Fact(action='find_disease'),Fact(g09="yes"))
	def disease_1(self):
		self.declare(Fact(disease="brown_spot"))
        
	@Rule(Fact(action='find_disease'),Fact(g14="yes"))
	def disease_2(self):
		self.declare(Fact(disease="narrow_brown_spot"))

	@Rule(Fact(action='find_disease'),Fact(g01="yes"),Fact(g20="yes"))
	def disease_3(self):
		self.declare(Fact(disease="sheath_bligh"))
        
	@Rule(Fact(action='find_disease'),Fact(g27="yes"))
	def disease_4(self):
		self.declare(Fact(disease="false_smut"))

	@Rule(Fact(action='find_disease'),Fact(g32="yes"),Fact(g33="yes"),Fact(g34="yes"))
	def disease_5(self):
		self.declare(Fact(disease="grassy_stunt"))
        
	@Rule(Fact(action='find_disease'),Fact(g20="yes"),Fact(g38="yes"))
	def disease_6(self):
		self.declare(Fact(disease="bacterial_leaf_blight"))

	@Rule(Fact(action='find_disease'),Fact(g32="yes"),Fact(g33="yes"),Fact(g43="yes"))
	def disease_7(self):
		self.declare(Fact(disease="tungro"))

	@Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)
	def disease(self, disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		print_details(id_disease, disease_details, treatments, 1)

	@Rule(Fact(action='find_disease'),
		  Fact(g01=MATCH.g01),
		  Fact(g02=MATCH.g02),
		  Fact(g09=MATCH.g09),
		  Fact(g14=MATCH.g14),
		  Fact(g20=MATCH.g20),
		  Fact(g27=MATCH.g27),
		  Fact(g32=MATCH.g32),
		  Fact(g33=MATCH.g33), 
		  Fact(g33=MATCH.g34),
		  Fact(g38=MATCH.g38),
		  Fact(g43=MATCH.g43),  
		  NOT(Fact(disease=MATCH.disease)),salience = -999)

	def not_matched(self,g01, g02, g09, g14, g20, g27, g32, g33, g34, g38, g43):
		print("\n" + color.BOLD + color.RED +  "We were unable to find any disease that exactly matching for given symptoms!" + color.END + color.END)
		lis = [g01, g02, g09, g14, g20, g27, g32, g33, g34, g38, g43]
		max_count = 0
		max_disease = ""
		for key,val in symptom_map.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "yes"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_disease = val
		if max_disease == "" :
			print("\n" + color.BOLD + "Try again with valid inputs..." + color.END) 
		else :
			if_not_matched(max_disease)

if __name__ == "__main__":
	preprocess()
	engine = Greetings()
	while(1):
		engine.reset()  # Prepare the engine for the execution.
		engine.run()  # Run it!
		time.sleep(2)
		print("", flush=True)
		if input(color.BOLD + color.BLUE + "Would you like to diagnose some other symptoms?" + color.END + color.END + " (yes/no) :") == "no":
			exit()
		#print(engine.facts)