# Fantasy Name Generator
A Python 3 script to train a recurrent neural network on a corpus of fantasy creature names and generate new names from that corpus. It uses textgenrnn and is heavily inspired by [Max Woolf's](http://minimaxir.com/) [pokemon-ai repo](https://github.com/minimaxir/pokemon-ai). The dataset comes from the [pathfinder SRD](http://www.d20pfsrd.com/bestiary/tools/monster-filter).

The name of this repo is technically a misnomer. You can use any dataset you want, so really this could be a name generator for anything! 

Just have a csv with a Name column in the data folder, set the parameters (mainly model name and paths) in the ..._config.py files at the top of the directory, and run fantasycreature_training.py and fantasycreature_generate.py. The former will create the model and output the weights, vocab, and model parameters and store them in the config folder, and the latter will generate 100 names from the model outputted into a text file at the top of the directory.

I wrote this code in windows, and was running into some bugs when trying to run the code in the git bash terminal, but when running through a python interpreter it works fine.

### Requirements
This repo requires the pandas and textgenrnn packages to be installed in python 3. Textgenrnn also has requirements that must be met.

### Usage
1. Use the provided dataset or place your own .csv file with a Name column in the data folder.
2. Change the parameters in fantasycreature_pretrain_config.py and fantasycreature_generate_config.py.
3. Run the fantasycreature_training.py script from the main directory in a python interpreter to train the model.
4. Run the fantasycreature_generate.py script from the main directory in a python interpretor to generate 500 names.

### Limitations
At least on my windows machine, the code does not seem to run properly when called in a git bash terminal.

Besides changing the dataset and path information in the configurations script, all other changes, such as parameter changes to the model, must be made in the training script.

### Examples
Here are 500 creatures produced from a training of the model with 200 epochs:

Old green dragon

Sealer

Migricine

Parga

Banner

Octoc

Shakoif

Great swarm

Aspi

Very old dragon

Death' azecad

Grayter swarm

Adult golem

Bores

Tendam

Very old quued beetle flob

Addus

Deep hunter elementalche dragon

Ancush

Ingy elemental

Adult shackling bourd

Young roncer popita

Giant positive energy elementaugher beetle

Cilatr swarm

Shira wolk of torm green dragon

Fire worman

Giant lightning sea snakker

Giant black dragon

Spath

Sangus mast

Greater elemental

Hawler

Taspling oaze

Part

Warer

Ancient squais wyrm black mast

Margita

Ghowlew

Young creep mantom

Giant elemental

Cran at

Marrasu

Giant blood manged emetat

Irclew

Shadow hunder

Mahure

Batste dragon

Theller devil

Large negative sephall elemental

Ice swarm

Timmon cuat

Stoimotan

Juvenile colota

Polsae

Mammoth

Kort

Dragon

Lilgungus

Shadow wolf

Alding marma

Lerger golem

Elder swarm

Warer

Shagari

Cise gray dragon

Vercap

Greater elemental

Shind brass dragon

Giant sea serpent

Acorpiker

Oct

Slaug

Keranggaller

Sark

Deliolequ

Thing winp

Cerstom

Mythic elemental

Adult red dragon

Nechwang bronze

Clood ooze

Very old creeper

Torvering blue dragon

Stole

Elcer

Giant mud elemental

Young elemental

Ock dragon

Thring crab, spider

Aldino

Urder

Adult sea sea serpling golem

Banthy

Stopositive spider whetle

Draconadaemon

Dire gylulus

Giant swarm

Kales

Tirder serpent

Juvine

Tant spider

Mythic mernon

Souandasu

Lesser dragon

Storm dragon

Raven spike red dragon

Deve

Juvenile copcangient

Giant bladodaemon

Seaher giant sea scorpion solak

Frork

Huge steerapeir

Trona

Shadow worm

Tightning elemental

Margu

Clockwork spawnes

Conar dragon

Death shask

Young olb dragon

Blood urch

Fire gargoyle

Frost dragon

Greater swarm

Mythic watergaanter barra

Ord

Giant amble

Very ooze

Lythic crab

Flases

Korps

Star crobon

Sea serpent

Adult golem

Undead

Greater horring

Raval

Phasous

Shipper dragon

Giant wight swarm

Shadown

Oross swarm

Great cyyppolid

Wilvone okas

Oll green dragon

Borelach dragon

Elder night

Giant ant sea serphe troll

Captintanf

Crimm

Hellow bese

Hengea

Greinger swarm

Marlor

Kunl

Silvere

Fire golem

Slarle

Carly blue dragon

The swarm

Thite swarm

Darcershaen

Sea sea swarm

Old blue light

Dreg warr

Lurar

Mond dant

Hangorm

Adult bragmy elemental

Adult golem

Manire elemental

Ancient molouc banromon

Large leegar

Vog

Belaem stor

Lerantud

Cave minotair elemental

Albing dragon

Adult green giant scabo

Rava

Medium spawner

Fudan

Devil

Phalider

Karabar ooze

Cuvemilictecitin

Jinx

Monstral dragon

Charing cattan

Young vyry brask dragon

Skig

Spider

Danwialterphinx

Small obri

Ancient hond

Juvenile sea serpel dragon

Henss

Wyrklider

Cloddeman

Wyrmligan

Dire stomairth noma

Young copper

Shadow wraitan beedle

Moner

Demon

Large leeph

Carniae quasi

Fasma

Medium oaze

Lick dragon

Barch

Kalto sard

Frost dragon

Stone budder arzosid bear

Small obazor dragon

Natiuer armon

Hunger crow

Blood mud elemental

Mah-thal

Parrack

Ircrant witchar

Conne golem

Zombar stor

Imprey

Slamprall

Lehantom armosiyn warpectre pat

Small spider

Stone skakaim

Dermagher giant oms

Witcer

Dowing

Giant swarm

Adult white swarm

Theling of titan

Small giant

Bog stuned

Mongosaurus

Nightning energy elemental

Young adult creep mumble

Greater elemental

Great wyrm bones

Chire lizard

Adult devil

Janing elemental

Ligir

Stakon

Flest dragon

Funguspider

Chore

Larre drake

Monset

Young bris

Ancient brass dragon

Shikon

Spider

Phrelisl

Juyn arch

Ligit cuser

Train ooze

Rablis

Strightning elemental

Clockwork span

Kerbank

Medium babe troll

Abers

Carele

Spinten spider

Cave moont

Nerra

Giant crawler

Dire elemental

Mythic fring bronz

Pherchon

Devil

Idule

Tixe

Stral candalion

Fere

Greater borg

Ancient bone of spider

Nald

Kalester

Adult white whate thollo

Pleel golem

Shaghael

Huge gray dragon

Wareripore gravity elemental

Wargoyle riget culas

Ancient soldier

Istardaanterdiend sea

The yra worm

Clobeatt

Beland

Elder ant swarm

Elder rora

Giant flen

Borest dragon

Juvenile elemental

Giant viper

Iran pudding

Hell magmit

Mamic cand

Thrram

Wyrmling righting seat wyrm black dragon

Hagant

Fanthon

Warewon

Ancient swarm

Urdralk

Sheant

Lorge

Ancient centto dragon

Chang

Huge dragon

Thengiter crowle dog

Adult stor

Hatut swarm

Deagh

Torting devil

Thone

Timming of spider

Phoran

Undead swarm

Kille drakei

Lergite

Ware

Than

Cathic faaceleswork dragon

Wyrmling hound gray dragon

Mythic hunter earth devil

Shard

Valpaen

Giant sea serpent

Manur

Formilacras

Witer

Lesser walr aroch swarm

Bater corbian quasi

Anose swarm

Shark

Kalus

fagwh

Creveer

Large gravity elemental

Carpiang monterl

Halk elemental

Greated frog

Old bree elemental

fire hag

Mosse

Young black dragon

Juvenile of therium

Shackain

Telran

Raval

Loran

Piter

Ooze

Small condation

Warer dragon

Phoar

Boue ountju skell

Graven spawn skoleftite dragon

Certous

Bagrind

Young olbera

Young brine old dragon

Young skur

Bernon

Cama demon

Large wasp

Adum

Shadow rone golem

Brass dragon

Trebinterous giant spider

Farphet spider

Aphierfal-nakd

Funche

Chole

Blood dragon

Adult whis

Eddler

Giant flecher

Craych dragon

Hanuner

Barponati

Young hart devil

Thetil

Huge mastrakk snake

Marden head skole

River dragon

Rake

Pant

Urder ight

Small obsidian

Nightning crow

Mythic miphie

Carsian dragon

Domonstronge

Plast man

Formion

Archer

Young dunger beetle

Young greater swarm

Verblosk

Giant pend

Phoric faling elemental

Funid

Giant sea dragon

Night

Reddemla

Great horsinkin cist

Trigan

Garda

Dracodaemon

Min sea sea treantl

Corre

Navous

Mardian dragon

Mythic fia

Winsllaus sea wasp

Train arch

Witch

Leant

Gray devil

Foras devil

Sea servadle dragon

Deant

Bone of scel gaant adult blie

Old grim

Phawl

Trenzioner

Giant creater slarge meer

Fire spider

Giant marma

Clockwork spirian

Medium bangover

Hell black dragon

Dark stee

Haven lat

Ravone golem

Juvenile lign dragon

Juvantling

Spice elemental

Jolin

Borble swarm

Nenision cyplotz carosh dragon

Clockwork dragon

Plastoden

Raven hostidar

Giant sea serpent

Ancient beetle

Adult suln

Medium mastiggai

Great dragon ooze

Charan

Grey snille stag beetle

Hanged gasp

Night

Manid

Kerm

Bloib gargoygeres

Staggath

Very of snake

Planter

Luster

Clow white dragon

Morkernite

Ice golem

Spire

Plicer bebal

Seaner

Nigat

Hound swarm

Giant bones

Giant rotan

Shadow white

Satal sea serpent

Tir gurcubius dag

Marto dragon

Cargoyle guard

Skential scair

Ancel pravant

Bleater borg of sky swarm

Spind anter linnorium

Very ypin

Omated erem

Dark dragon

Pathan

Scorbsning earth gylasin queentie

Devourforne devil

Giant crow

Monstoak

Chore coly ctil

Night

Borbery

Livith man

Magmot

Worm oca


