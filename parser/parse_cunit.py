import json

def CUnitMember(offset):
    return [offset, "4", True]

def Member(offset, kind):
    return [offset, kind, True]

def UnsupportedMember(offset, kind):
    return [offset, kind, False]

unitdict = {}
unitdict["prev"] = CUnitMember(0x000)
unitdict["next"] = CUnitMember(0x004)  # link
# displayed value is ceil(healthPoints/256)
unitdict["hp"] = Member(0x008, "4")
unitdict["sprite"] = CUnitMember(0x00C)
unitdict["moveTargetPos"] = Member(0x010, "2x2")
unitdict["moveTargetX"] = Member(0x010, "2")
unitdict["moveTargetY"] = Member(0x012, "2")
unitdict["moveTarget"] = CUnitMember(0x014)
unitdict["moveTargetUnit"] = CUnitMember(0x014)
# The next way point in the path the unit is following to get to
# its destination. Equal to moveToPos for air units since they
# don't need to navigate around buildings.
unitdict["nextMovementWaypoint"] = Member(0x018, "2x2")
# The desired position
unitdict["nextTargetWaypoint"] = Member(0x01C, "2x2")
unitdict["movementFlags"] =  Member(0x020, "1")
# current direction the unit is facing
unitdict["currentDirection1"] = Member(0x021, "1")
unitdict["turnRadius"] = Member(0x022, "1")  # flingy
# usually only differs from the currentDirection field for units that
# can accelerate and travel in a different direction than they are facing.
# For example Mutalisks can change the direction they are facing
# faster than then can change the direction they are moving.
unitdict["velocityDirection1"] = Member(0x023, "1")
unitdict["flingyID"] = Member(0x024, "2")
unitdict["unknown0x26"] = Member(0x026, "1")
unitdict["flingyMovementType"] = Member(0x027, "1")
# Current position of the unit
unitdict["pos"] = Member(0x028, "2x2")
unitdict["posX"] = Member(0x028, "2")
unitdict["posY"] = Member(0x02A, "2")
unitdict["haltX"] = Member(0x02C, "4")
unitdict["haltY"] = Member(0x030, "4")
unitdict["topSpeed"] = Member(0x034, "4")
unitdict["currentSpeed1"] = Member(0x038, "4")
unitdict["currentSpeed2"] = Member(0x03C, "4")
unitdict["currentVelocityX"] = Member(0x040, "4")
unitdict["currentVelocityY"] = Member(0x044, "4")
unitdict["acceleration"] = Member(0x048, "2")
unitdict["currentDirection2"] = Member(0x04A, "1")
unitdict["velocityDirection2"] = Member(0x04B, "1")  # pathing related
unitdict["playerID"] = Member(0x04C, "1")
unitdict["owner"] = Member(0x04C, "1")
unitdict["orderID"] = Member(0x04D, "1")
unitdict["order"] = Member(0x04D, "1")
unitdict["orderState"] = Member(0x04E, "1")
unitdict["orderSignal"] = Member(0x04F, "1")
unitdict["orderUnitType"] = Member(0x050, "2")
unitdict["unknown0x52"] = Member(0x052, "2")  # 2-byte padding
unitdict["cooldown"] = Member(0x054, "4")
unitdict["orderTimer"] = Member(0x054, "1")
unitdict["gCooldown"] = Member(0x055, "1")
unitdict["aCooldown"] = Member(0x056, "1")
unitdict["spellCooldown"] = Member(0x057, "1")
unitdict["groundWeaponCooldown"] = Member(0x055, "1")
unitdict["airWeaponCooldown"] = Member(0x056, "1")
unitdict["orderTargetPos"] = Member(0x058, "2x2")  # ActionFocus
unitdict["orderTargetXY"] = Member(0x058, "2x2")
unitdict["orderTargetX"] = Member(0x058, "2")
unitdict["orderTargetY"] = Member(0x05A, "2")
unitdict["orderTarget"] = CUnitMember(0x05C)
unitdict["orderTargetUnit"] = CUnitMember(0x05C)
unitdict["shield"] = Member(0x060, "4")
unitdict["unitID"] = Member(0x064, "2")
unitdict["unitType"] = Member(0x064, "2")
unitdict["unknown0x66"] = Member(0x066, "2")  # 2-byte padding
unitdict["prevPlayerUnit"] = CUnitMember(0x068)
unitdict["nextPlayerUnit"] = CUnitMember(0x06C)
unitdict["subUnit"] = CUnitMember(0x070)
unitdict["orderQueueHead"] = UnsupportedMember(0x074, "4")  # COrder
unitdict["orderQueueTail"] = UnsupportedMember(0x078, "4")
unitdict["autoTargetUnit"] = CUnitMember(0x07C)
# larva, in-transit, addons
unitdict["connectedUnit"] = CUnitMember(0x080)
# may be count in addition to first since can be 2 when 3 orders are queued
unitdict["orderQueueCount"] = Member(0x084, "1")
# Cycles down from from 8 to 0 (inclusive). See also 0x122.
unitdict["orderQueueTimer"] = Member(0x085, "1")
unitdict["unknown0x86"] = Member(0x086, "1")
# Prevent "Your forces are under attack."] on every attack
unitdict["attackNotifyTimer"] = Member(0x087, "1")
# zerg buildings while morphing
unitdict["prevUnitType"] = UnsupportedMember(0x088, "2")
unitdict["lastEventTimer"] = UnsupportedMember(0x08A, "1")
# 17"] = was completed (train, morph), 174"] = was attacked
unitdict["lastEventColor"] = UnsupportedMember(0x08B, "1")
#  might have originally been RGB from lastEventColor
unitdict["unknown0x8C"] = Member(0x08C, "2")
unitdict["rankIncrease"] = Member(0x08E, "1")
unitdict["killCount"] = Member(0x08F, "1")
unitdict["lastAttackingPlayer"] = Member(0x090, "1")
unitdict["secondaryOrderTimer"] = Member(0x091, "1")
unitdict["AIActionFlag"] = Member(0x092, "1")
# 2"] = issued an order
# 3"] = interrupted an order
# 4"] = hide self before death (self-destruct?)
unitdict["userActionFlags"] = Member(0x093, "1")
unitdict["currentButtonSet"] = Member(0x094, "2")
unitdict["isCloaked"] = Member(0x096, "1")
unitdict["movementState"] = Member(0x097, "1")
unitdict["buildQueue1"] = Member(0x098, "2")
unitdict["buildQueue2"] = Member(0x09A, "2")
unitdict["buildQueue3"] = Member(0x09C, "2")
unitdict["buildQueue4"] = Member(0x09E, "2")
unitdict["buildQueue5"] = Member(0x0A0, "2")
unitdict["buildQueue12"] = Member(0x098, "4")
unitdict["buildQueue34"] = Member(0x09C, "4")
unitdict["energy"] = Member(0x0A2, "2")
unitdict["buildQueueSlot"] = Member(0x0A4, "1")
unitdict["targetOrderSpecial"] = Member(0x0A5, "1")
unitdict["uniquenessIdentifier"] = Member(0x0A5, "1")
unitdict["secondaryOrder"] = Member(0x0A6, "1")
unitdict["secondaryOrderID"] = Member(0x0A6, "1")
# 0 means the building has the largest amount of fire/blood
unitdict["buildingOverlayState"] = Member(0x0A7, "1")
unitdict["hpGain"] = Member(0x0A8, "2")  # buildRepairHpGain
unitdict["shieldGain"] = Member(0x0AA, "2")  # Shield gain on construction
# Remaining bulding time; also used by powerups (flags)
# as the timer for returning to their original location.
unitdict["remainingBuildTime"] = Member(0x0AC, "2")
#  The HP of the unit before it changed
# (example Drone->Hatchery, the Drone's HP will be stored here)
unitdict["prevHp"] = Member(0x0AE, "2")
# alphaID (StoredUnit)
unitdict["loadedUnit1"] = UnsupportedMember(0x0B0, "2")
unitdict["loadedUnit2"] = UnsupportedMember(0x0B2, "2")
unitdict["loadedUnit3"] = UnsupportedMember(0x0B4, "2")
unitdict["loadedUnit4"] = UnsupportedMember(0x0B6, "2")
unitdict["loadedUnit5"] = UnsupportedMember(0x0B8, "2")
unitdict["loadedUnit6"] = UnsupportedMember(0x0BA, "2")
unitdict["loadedUnit7"] = UnsupportedMember(0x0BC, "2")
unitdict["loadedUnit8"] = UnsupportedMember(0x0BE, "2")
# union (0xC0 ~ 0xCF) //==================================
unitdict["spiderMineCount"] = Member(0x0C0, "1")  # vulture
# carrier, reaver ----------------------------------------
unitdict["inHangarChild"] = CUnitMember(0x0C0)
unitdict["outHangarChild"] = CUnitMember(0x0C4)
unitdict["inHangarCount"] = Member(0x0C8, "1")
unitdict["outHangarCount"] = Member(0x0C9, "1")
# interceptor, scarab ------------------------------------
unitdict["parent"] = CUnitMember(0x0C0)
unitdict["prevFighter"] = CUnitMember(0x0C4)
unitdict["nextFighter"] = CUnitMember(0x0C8)
unitdict["isOutsideHangar"] = Member(0x0CC, "1")
# beacon -------------------------------------------------
unitdict["beaconUnknown0xC0"] = Member(0x0C0, "4")
unitdict["beaconUnknown0xC4"] = Member(0x0C4, "4")
unitdict["flagSpawnFrame"] = Member(0x0C8, "4")  # beacon
# building /==============================================
unitdict["addon"] = CUnitMember(0x0C0)
unitdict["addonBuildType"] = Member(0x0C4, "2")
unitdict["upgradeResearchTime"] = Member(0x0C6, "2")
unitdict["techType"] = Member(0x0C8, "1")
unitdict["upgradeType"] = Member(0x0C9, "1")
unitdict["larvaTimer"] = Member(0x0CA, "1")
unitdict["landingTimer"] = Member(0x0CB, "1")
unitdict["creepTimer"] = Member(0x0CC, "1")
unitdict["upgradeLevel"] = Member(0x0CD, "1")
# padding0xCE
# resource -----------------------------------------------
unitdict["resourceAmount"] = Member(0x0D0, "2")  # 0x0D0 union
unitdict["resourceIscript"] = Member(0x0D2, "1")
unitdict["gatherQueueCount"] = Member(0x0D3, "1")
# pointer to the next worker unit waiting in line to gather
unitdict["nextGatherer"] = CUnitMember(0x0D4)
unitdict["resourceGroup"] = Member(0x0D8, "1")
unitdict["resourceBelongsToAI"] = Member(0x0D9, "1")
# other buildings ----------------------------------------
unitdict["nydusExit"] = CUnitMember(0x0D0)  # connected nydus canal
# confirmed to be CUnit* and not CSprite*
unitdict["ghostNukeMissile"] = Member(0x0D0, "4")
unitdict["pylonAura"] = Member(0x0D0, "4")
# silo
unitdict["siloNuke"] = CUnitMember(0x0D0)
unitdict["siloReady"] = Member(0x0D4, "1")
# hatchery
unitdict["hatcheryHarvestL"] = Member(0x0D0, "2")
unitdict["hatcheryHarvestU"] = Member(0x0D2, "2")
unitdict["hatcheryHarvestR"] = Member(0x0D4, "2")
unitdict["hatcheryHarvestB"] = Member(0x0D6, "2")
unitdict["hatcheryHarvestLU"] = Member(0x0D0, "4")
unitdict["hatcheryHarvestRB"] = Member(0x0D4, "4")
# ==============================================/ building
# worker -------------------------------------------------
unitdict["powerup"] = CUnitMember(0x0C0)
unitdict["targetResourcePos"] = Member(0x0C4, "2x2")
unitdict["targetResourceX"] = Member(0x0C4, "2")
unitdict["targetResourceY"] = Member(0x0C6, "2")
unitdict["targetResourceUnit"] = CUnitMember(0x0C8)
unitdict["repairResourceLossTimer"] = Member(0x0CC, "2")
unitdict["isCarryingSomething"] = Member(0x0CE, "1")
unitdict["resourceCarryAmount"] = Member(0x0CF, "1")  # worker
unitdict["harvestTarget"] = CUnitMember(0x0D0)
unitdict["prevHarvestUnit"] = CUnitMember(0x0D4)
unitdict["nextHarvestUnit"] = CUnitMember(0x0D8)  # When there is a gather conflict
# powerup ------------------------------------------------
unitdict["powerupOrigin"] = Member(0x0D0, "2x2")
unitdict["powerupOriginX"] = Member(0x0D0, "2")
unitdict["powerupOriginY"] = Member(0x0D2, "2")  # powerup
unitdict["powerupCarryingUnit"] = CUnitMember(0x0D4)
# \\\\\\\\\\\\\\\=================================// union
unitdict["statusFlags"] = Member(0x0DC, "4")
# Type of resource chunk carried by this worker.
# None"] = 0x00,
# Vespene"] = 0x01,
# Minerals"] = 0x02,
# GasOrMineral"] = 0x03,
# PowerUp"] = 0x04
unitdict["resourceType"] = Member(0x0E0, "1")
unitdict["wireframeRandomizer"] = Member(0x0E1, "1")
unitdict["secondaryOrderState"] = Member(0x0E2, "1")
# Counts down from 15 to 0 when most orders are given,
# or when the unit moves after reaching a patrol location
unitdict["recentOrderTimer"] = Member(0x0E3, "1")
# which players can detect this unit (cloaked/burrowed)
unitdict["visibilityStatus"] = Member(0x0E4, "4")
unitdict["secondaryOrderPos"] = Member(0x0E8, "2x2")
unitdict["secondaryOrderX"] = Member(0x0E8, "2")
unitdict["secondaryOrderY"] = Member(0x0EA, "2")
unitdict["currentBuildUnit"] = CUnitMember(0x0EC)
unitdict["prevBurrowedUnit"] = UnsupportedMember(0x0F0, "4")
unitdict["nextBurrowedUnit"] = UnsupportedMember(0x0F4, "4")
unitdict["rallyPos"] = Member(0x0F8, "2x2")
unitdict["rallyX"] = Member(0x0F8, "2")
unitdict["rallyY"] = Member(0x0FA, "2")
unitdict["rallyUnit"] = CUnitMember(0x0FC)
unitdict["prevPsiProvider"] = CUnitMember(0x0F8)  # not supported?
unitdict["nextPsiProvider"] = CUnitMember(0x0FC)
unitdict["path"] = UnsupportedMember(0x100, "4")
unitdict["pathingCollisionInterval"] = Member(0x104, "1")
# 0x01"] = uses pathing; 0x02"] = ?; 0x04"] = ?
unitdict["pathingFlags"] = Member(0x105, "1")
unitdict["unknown0x106"] = Member(0x106, "1")
# 1 if a medic is currently healing this unit
unitdict["isBeingHealed"] = Member(0x107, "1")
# A rect that specifies the closest contour (collision) points
unitdict["contourBoundsLU"] = UnsupportedMember(0x108, "4")
unitdict["contourBoundsL"] = UnsupportedMember(0x108, "2")
unitdict["contourBoundsU"] = UnsupportedMember(0x10A, "2")
unitdict["contourBoundsRB"] = UnsupportedMember(0x10C, "4")
unitdict["contourBoundsR"] = UnsupportedMember(0x10C, "2")
unitdict["contourBoundsB"] = UnsupportedMember(0x10E, "2")
# Hallucination, Dark Swarm, Disruption Web, Broodling
# (but not Scanner Sweep according to BWAPI)
unitdict["removeTimer"] = Member(0x110, "2")
unitdict["defensiveMatrixHp"] = Member(0x112, "2")
unitdict["defensiveMatrixTimer"] = Member(0x114, "1")
unitdict["stimTimer"] = Member(0x115, "1")
unitdict["ensnareTimer"] = Member(0x116, "1")
unitdict["lockdownTimer"] = Member(0x117, "1")
unitdict["irradiateTimer"] = Member(0x118, "1")
unitdict["stasisTimer"] = Member(0x119, "1")
unitdict["plagueTimer"] = Member(0x11A, "1")
unitdict["stormTimer"] = Member(0x11B, "1")
# Used to tell if a unit is under psi storm	(is "stormTimer"] in BWAPI)
unitdict["isUnderStorm"] = Member(0x11B, "1")
unitdict["irradiatedBy"] = CUnitMember(0x11C)
unitdict["irradiatePlayerID"] = Member(0x120, "1")
# Each bit corresponds to the player who has parasited this unit
unitdict["parasiteFlags"] = Member(0x121, "1")
# counts/cycles up from 0 to 7 (inclusive). See also 0x85
unitdict["cycleCounter"] = Member(0x122, "1")
# Each bit corresponds to the player who has optical flared this unit
unitdict["blindFlags"] = Member(0x123, "1")  # bool in BWAPI
unitdict["maelstromTimer"] = Member(0x124, "1")
# Might be afterburner timer or ultralisk roar timer
unitdict["unusedTimer"] = Member(0x125, "1")
unitdict["acidSporeCount"] = Member(0x126, "1")
unitdict["acidSporeTime0"] = Member(0x127, "1")
unitdict["acidSporeTime1"] = Member(0x128, "1")
unitdict["acidSporeTime2"] = Member(0x129, "1")
unitdict["acidSporeTime3"] = Member(0x12A, "1")
unitdict["acidSporeTime4"] = Member(0x12B, "1")
unitdict["acidSporeTime5"] = Member(0x12C, "1")
unitdict["acidSporeTime6"] = Member(0x12D, "1")
unitdict["acidSporeTime7"] = Member(0x12E, "1")
unitdict["acidSporeTime8"] = Member(0x12F, "1")
# Cycles between 0-12 for each bullet fired by this unit
# (if it uses a "Attack 3x3 area"] weapon)
unitdict["offsetIndex3by3"] = UnsupportedMember(0x130, "2")
unitdict["unknown0x132"] = UnsupportedMember(0x132, "2")  # padding
unitdict["AI"] = UnsupportedMember(0x134, "4")
unitdict["airStrength"] = UnsupportedMember(0x138, "2")
unitdict["groundStrength"] = UnsupportedMember(0x13A, "2")
unitdict["finderIndexLeft"] = UnsupportedMember(0x13C, "4")
unitdict["finderIndexRight"] = UnsupportedMember(0x140, "4")
unitdict["finderIndexTop"] = UnsupportedMember(0x144, "4")
unitdict["finderIndexBottom"] = UnsupportedMember(0x148, "4")
# updated only when air unit is being pushed
unitdict["repulseUnknown"] = Member(0x14C, "1")
unitdict["repulseAngle"] = Member(0x14D, "1")
unitdict["driftPos"] = Member(0x14E, "2")  # (mapsizex / 1.5 max)
unitdict["driftX"] = Member(0x14E, "1")
unitdict["driftY"] = Member(0x14F, "1")
unitdict["UNKNOWN"] = Member(0x150, "1")

with open("Offset_CUnit_original.json", "rt") as file:
    arr = json.load(file)

newarr = []
for a in arr:
    if a["version"] == "1.16.1":
        offset = int(a["address"]) - 5885096
        for key, value in unitdict.items():
            if value[0] == offset:
                break
        a["varname"] = key
        a["scr"] = "Supported" if value[2] else "Unsupported"
        a["size"] = value[1]
        a["offset"] = "0x%03X" % offset
        newarr.append(a)


newarr.sort(key=lambda i: int(i["address"]))

with open("Offset_CUnit.json", "wt") as file:
    json.dump(newarr, file, indent="    ")
