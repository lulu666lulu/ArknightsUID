from msgspec import Struct, field


################
# ArknightsAttendanceCalendar Start
################
class ArknightsAttendanceAwardResource(Struct):
    id_: str = field(name='id')
    type_: str = field(name='type')
    name: str
    rarity: int


class ArknightsAttendanceRecord(Struct):
    ts: str
    resourceId: str
    type_: str = field(name='type')
    count: int


class ArknightsAttendanceCalendar(Struct):
    resourceId: str
    type_: str = field(name='type')
    count: int
    available: bool
    done: bool


class ArknightsAttendanceCalendarModel(Struct):
    currentTs: str
    calendar: list[ArknightsAttendanceCalendar]
    records: list[ArknightsAttendanceRecord | None]
    resourceInfoMap: dict[str, ArknightsAttendanceAwardResource]


################
# ArknightsAttendance Start
################
class ArknightsAttendanceAward(Struct):
    resource: ArknightsAttendanceAwardResource
    count: int
    type_: str = field(name='type')

class ArknightsAttendanceModel(Struct):
    ts: str
    awards: list[ArknightsAttendanceAward]
################
# ArknightsAttendance End
################



################
# ArknightsUserMeModel Start
################

class UserMeInfoApply(Struct):
    nickname: str
    profile: str


class UserMeModerator(Struct):
    isModerator: bool


class UserGameStatusAp(Struct):
    current: int
    max_: int = field(name='max')
    lastApAddTime: int
    completeRecoveryTime: int


class UserGameStatusSecretary(Struct):
    charId: str
    skinId: str


class UserGameStatusAvatar(Struct):
    type_: str = field(name='type')
    id_: str = field(name='id')


class UserGameStatus(Struct):
    uid: str
    name: str
    level: int
    registerTs: int
    mainStageProgress: str
    secretary: UserGameStatusSecretary
    resume: str
    subscriptionEnd: int
    ap: UserGameStatusAp
    storeTs: int
    lastOnlineTs: int
    charCnt: int
    furnitureCnt: int
    skinCnt: int
    avatar: UserGameStatusAvatar | None = None


class UserMeInfoRts(Struct):
    liked: str
    collect: str
    comment: str
    follow: str
    fans: str
    black: str
    pub: str


class UserMeInfo(Struct):
    id_: str = field(name='id')
    nickname: str
    profile: str
    avatarCode: int
    avatar: str
    backgroundCode: int
    isCreator: bool
    creatorIdentifiers: list[str]
    status: int
    operationStatus: int
    identity: int
    kind: int
    latestIpLocation: str
    moderatorStatus: int
    moderatorChangeTime: int
    gender: int
    birthday: str


class ArknightsUserMeModel(Struct, omit_defaults=True):
    user: UserMeInfo
    userRts: UserMeInfoRts
    userSanctionList: list[str]
    gameStatus: UserGameStatus
    moderator: UserMeModerator
    userInfoApply: UserMeInfoApply

################
# ArknightsUserMeModel End
################



################
# ArknightsPlayerInfoModel Start
################

class PlayerManufactureFormulaInfo(Struct):
    id_: str = field(name='id')
    itemId: str
    count: int
    weight: int
    costPoint: int
    costs: list[str] | None = None


class PlayerEquipmentInfo(Struct):
    id_: str = field(name='id')
    name: str
    typeIcon: str
    shiningColor: str
    desc: str | None = None
    typeName1: str | None = None


class PlayerCampaignZoneInfo(Struct):
    id_: str = field(name='id')
    name: str


class PlayerMedalInfo(Struct):
    pass


class PlayerCampaignInfo(Struct):
    id_: str = field(name='id')
    name: str
    campaignZoneId: str


class PlayerRogueInfo(Struct):
    id_: str = field(name='id')
    name: str
    sort: int


class PlayerTowerInfo(Struct):
    id_: str = field(name='id')
    name: str
    subName: str
    hasHard: bool | None = None
    stageNum: int | None = None


class PlayerZoneInfo(Struct):
    id_: str = field(name='id')
    name: str


class PlayerActivityInfo(Struct):
    id_: str = field(name='id')
    name: str
    startTime: int
    endTime: int
    rewardEndTime: int
    isReplicate: bool
    type_: str = field(name='type')


class PlayerStageInfo(Struct):
    id_: str = field(name='id')
    code: str
    name: str


class PlayerSkinInfo(Struct):
    id_: str = field(name='id')
    brandId: str
    sortId: int
    displayTagId: str
    name: str | None = None
    brandName: str | None = None
    brandCapitalName: str | None = None
    illustId: str | None = None
    dynIllustId: str | None = None
    avatarId: str | None = None
    portraitId: str | None = None
    skinGroupId: str | None = None


class PlayerCharInfo(Struct):
    id_: str = field(name='id')
    name: str
    nationId: str
    groupId: str
    displayNumber: str
    rarity: int
    profession: str
    subProfessionId: str


class ActivityZoneStageStatus(Struct):
    stageId: str
    completed: bool


class ActivityZone(Struct):
    zoneId: str
    zoneReplicaId: str
    clearedStage: int
    totalStage: int
    stageStatus: list[ActivityZoneStageStatus] | None = None


class PlayerActivity(Struct):
    actId: str
    actReplicaId: str
    zones: list[ActivityZone]
    type_: str | None = field(name='type', default=None)


class RewoardItem(Struct):
    current: int
    total: int


class PlayerRoutine(Struct):
    daily: RewoardItem
    weekly: RewoardItem


class BankItem(Struct):
    current: int
    record: int


class RogueRecord(Struct):
    rogueId: str
    relicCnt: int
    bank: BankItem
    mission: RewoardItem | None = None
    clearTime: int | None = None


class PlayerRogue(Struct):
    records: list[RogueRecord]


class TowerReward(Struct):
    higherItem: RewoardItem
    lowerItem: RewoardItem
    termTs: int


class TowerRecord(Struct):
    towerId: str
    best: int
    hasHard: bool | None = None
    stageNum: int | None = None
    unlockHard: bool | None = None
    hardBest: int | None = None


class PlayerTower(Struct):
    records: list[TowerRecord]
    reward: TowerReward


class CampaignReward(Struct):
    current: int
    total: int


class CampaignRecord(Struct):
    campaignId: str
    maxKills: int


class PlayerCampaign(Struct):
    records: list[CampaignRecord]
    reward: CampaignReward


class RecruitTag(Struct):
    tagId: int
    pick: int


class PlayerRecruit(Struct):
    startTs: int
    finishTs: int
    state: int
    duration: int | None = None
    selectTags: list[RecruitTag] | None = None


class BuildingTrainingTrainee(Struct):
    charId: str
    targetSkill: int
    ap: int
    lastApAddTime: int


class BuildingTrainingTrainer(Struct):
    charId: str
    ap: int
    lastApAddTime: int


class BuildingClue(Struct):
    own: int
    received: int
    dailyReward: bool
    needReceive: int
    board: list[str]
    sharing: bool
    shareCompleteTime: int


class BuildingCharBubbleInfo(Struct):
    add: int
    ts: int


class BuildingCharBubble(Struct):
    normal: BuildingCharBubbleInfo
    assist: BuildingCharBubbleInfo


class BuildingChar(Struct):
    charId: str
    ap: int
    lastApAddTime: int
    index: int
    bubble: BuildingCharBubble
    workTime: int


class BuildingControl(Struct):
    slotId: str
    slotState: int
    level: int
    chars: list[BuildingChar]


class BuildingCorridor(Struct):
    slotId: str
    slotState: int
    level: int


class BuildingElevator(Struct):
    slotId: str
    slotState: int
    level: int


class BuildingFurniture(Struct):
    total: int


class BuildingLabor(Struct):
    maxValue: int
    value: int
    lastUpdateTime: int
    remainSecs: int


class BuildingTraining(Struct):
    slotId: str
    level: int
    trainee: BuildingTrainingTrainee
    remainPoint: float
    speed: float
    lastUpdateTime: int
    remainSecs: int
    slotState: int
    trainer: BuildingTrainingTrainer | None = None


class BuildingHire(Struct):
    slotId: str
    level: int
    chars: list[BuildingChar]
    state: int
    refreshCount: int
    completeWorkTime: int
    slotState: int


class BuildingMeeting(Struct):
    slotId: str
    level: int
    chars: list[BuildingChar]
    clue: BuildingClue
    lastUpdateTime: int
    completeWorkTime: int


class BuildingDormitories(Struct):
    slotId: str
    level: int
    chars: list[BuildingChar]
    comfort: int


class BuildingStockDelivery(Struct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


class BuildingStock(Struct):
    instId: int
    type_: str = field(name='type')
    delivery: list[BuildingStockDelivery]
    gain: BuildingStockDelivery
    isViolated: bool


class BuildingTradings(Struct):
    slotId: str
    level: int
    chars: list[BuildingChar]
    completeWorkTime: int
    lastUpdateTime: int
    strategy: str
    stock: list[BuildingStock]
    stockLimit: int


class BuildingManufactures(Struct):
    slotId: str
    level: int
    chars: list[BuildingChar]
    completeWorkTime: int
    lastUpdateTime: int
    formulaId: str
    capacity: int
    weight: int
    complete: int
    remain: int
    speed: float


class BuildingPower(Struct):
    slotId: str
    level: int
    chars: list[BuildingChar]


class BuildingTiredChar(Struct):
    charId: str
    ap: int
    lastApAddTime: int
    roomSlotId: str
    index: int
    bubble: BuildingCharBubble
    workTime: int


class PlayerBuilding(Struct):
    tiredChars: list[BuildingTiredChar]
    powers: list[BuildingPower]
    manufactures: list[BuildingManufactures]
    tradings: list[BuildingTradings]
    dormitories: list[BuildingDormitories]
    meeting: BuildingMeeting
    hire: BuildingHire
    labor: BuildingLabor
    furniture: BuildingFurniture
    elevators: list[BuildingElevator]
    corridors: list[BuildingCorridor]
    control: BuildingControl
    training: BuildingTraining | None = None


class PlayerInfoSkin(Struct):
    id_: str = field(name='id')
    ts: int


class PlayerInfoCharSkill(Struct):
    id_: str = field(name='id')
    specializeLevel: int


class PlayerInfoCharEquip(Struct):
    id_: str = field(name='id')
    level: int


class PlayerInfoChar(Struct):
    charId: str
    skinId: str
    level: int
    evolvePhase: int
    potentialRank: int
    mainSkillLvl: int
    skills: list[PlayerInfoCharSkill] | None
    equip: list[PlayerInfoCharEquip] | None
    favorPercent: int
    defaultSkillId: str
    gainTime: int
    defaultEquipId: str


class PlayerAssistCharEquip(Struct):
    id_: str = field(name='id')
    level: int


class PlayerAssistChar(Struct):
    charId: str
    skinId: str
    level: int
    evolvePhase: int
    potentialRank: int
    skillId: str
    mainSkillLvl: int
    specializeLevel: int
    equip: PlayerAssistCharEquip | None


class PlayerMedal(Struct):
    type_: str = field(name='type')
    template: str
    templateMedalList: list[str]
    customMedalLayout: list[str | None]
    total: int


class PlayerStatusAp(Struct):
    current: int
    max: int
    lastApAddTime: int
    completeRecoveryTime: int


class PlayerStatusSecretary(Struct):
    charId: str
    skinId: str


class PlayerStatusAvatar(Struct):
    type_: str = field(name='type')
    id_: str = field(name='id')


class PlayerStatus(Struct):
    uid: str
    name: str
    level: int
    registerTs: int
    mainStageProgress: str
    secretary: PlayerStatusSecretary
    resume: str
    subscriptionEnd: int
    ap: PlayerStatusAp
    storeTs: int
    lastOnlineTs: int
    charCnt: int
    furnitureCnt: int
    skinCnt: int
    avatar: PlayerStatusAvatar | None = None


class DisplayShowConfig(Struct):
    charSwitch: bool
    skinSwitch: bool
    standingsSwitch: bool


class PlayerActivityBannerList(Struct):
    activityId: str
    imgUrl: str
    url: str
    startTs: int
    endTs: int


class ArknightsPlayerInfoModel(Struct, omit_defaults=True, gc=False):
    currentTs: int
    showConfig: DisplayShowConfig
    status: PlayerStatus
    assistChars: list[PlayerAssistChar]
    chars: list[PlayerInfoChar]
    skins: list[PlayerInfoSkin]
    building: PlayerBuilding
    recruit: list[PlayerRecruit]
    campaign: PlayerCampaign
    tower: PlayerTower
    rogue: PlayerRogue
    routine: PlayerRoutine
    activity: list[PlayerActivity]
    charInfoMap: dict[str, PlayerCharInfo]
    skinInfoMap: dict[str, PlayerSkinInfo]
    stageInfoMap: dict[str, PlayerStageInfo]
    activityInfoMap: dict[str, PlayerActivityInfo]
    towerInfoMap: dict[str, PlayerTowerInfo]
    rogueInfoMap: dict[str, PlayerRogueInfo]
    campaignInfoMap: dict[str, PlayerCampaignInfo]
    campaignZoneInfoMap: dict[str, PlayerCampaignZoneInfo]
    equipmentInfoMap: dict[str, PlayerEquipmentInfo]
    manufactureFormulaInfoMap: dict[str, PlayerManufactureFormulaInfo]
    charAssets: list[str | None]
    skinAssets: list[str | None]
    activityBannerList: dict[str, list[PlayerActivityBannerList]]
    medal: PlayerMedal | None = None
    zoneInfoMap: dict[str, PlayerZoneInfo] | None = None
    medalInfoMap: dict[str, PlayerMedalInfo] | None = None


################
# ArknightsPlayerInfoModel End
################
